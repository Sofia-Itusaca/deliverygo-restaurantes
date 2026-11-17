#!/usr/bin/env python3
"""Validate local DeliveryGo SPEC completeness and this repository's CI contract."""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

SPEC_IDS = tuple(f"SPEC-{number:02d}" for number in range(1, 14))
REQUIRED_SECTIONS = (
    "Objetivo", "Alcance", "Descripcion", "Requisitos relacionados",
    "Restricciones", "Criterios de aceptacion", "Evidencias",
    "Especificaciones relacionadas",
)
PROJECT = Path(__file__).resolve().parents[1]
EXPECTED_REPOSITORY = "deliverygo-restaurantes"
EXPECTED_DEPLOYMENT = "deliverygo-restaurantes"
WORKFLOW_GATES = (
    "dotnet restore",
    "dotnet build",
    "dotnet test",
    "docker/build-push-action",
    "trivy",
)


def spec_presence_error(spec_id: str, count: int) -> str | None:
    return None if count == 1 else f"expected exactly one {spec_id}, found {count}"


def spec_content_errors(name: str, spec_id: str, content: str) -> list[str]:
    normalized = unicodedata.normalize("NFKD", content).encode("ascii", "ignore").decode("ascii")
    errors: list[str] = []
    if not re.search(rf"(?m)^# {re.escape(spec_id)}\b", normalized):
        errors.append(f"{name}: title does not identify {spec_id}")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"(?im)^##\s+{re.escape(section)}", normalized):
            errors.append(f"{name}: missing required section {section}")
    return errors


def workflow_contract_errors(workflow: str, ci_spec: str) -> list[str]:
    errors: list[str] = []
    for gate in WORKFLOW_GATES:
        if gate.casefold() not in workflow.casefold():
            errors.append(f"CI workflow missing required project gate: {gate}")
    if "python scripts/verify_specs.py" not in workflow:
        errors.append("CI workflow does not execute the SPEC verifier")
    if EXPECTED_REPOSITORY not in ci_spec:
        errors.append(f"SPEC-10 must document this repository's ECR repository {EXPECTED_REPOSITORY}")
    deploy = workflow.split("\n  deploy:", 1)
    if len(deploy) != 2:
        errors.append("workflow must keep a separate deploy job")
        return errors
    deploy_job = deploy[1].casefold()
    if EXPECTED_REPOSITORY not in deploy_job or EXPECTED_DEPLOYMENT not in deploy_job:
        errors.append("deploy job is not scoped to this repository's ECR repository and Deployment")
    if "vars.aws_deploy_enabled == 'true'" not in deploy_job:
        errors.append("deploy job must remain disabled unless AWS_DEPLOY_ENABLED is true")
    if "github.event_name == 'workflow_dispatch'" not in deploy_job or "inputs.deploy_production == true" not in deploy_job:
        errors.append("deploy job must require manual dispatch with deploy_production=true")
    if "vars.ecr_repository == '" + EXPECTED_REPOSITORY + "'" not in deploy_job:
        errors.append("deploy job must require this repository's exact ECR_REPOSITORY")
    apply_commands = re.findall(r"(?im)^\s*-?\s*run:\s*.*kubectl apply([^\r\n]*)", deploy_job)
    if not apply_commands or any(
        "-f k8s/namespace.yaml -f k8s/deployment.yaml -n deliverygo" not in command
        for command in apply_commands
    ):
        errors.append("deploy job must apply only this repository's Kubernetes manifests")
    return errors


def manifest_contract_errors(manifest: str) -> list[str]:
    errors: list[str] = []
    resources = re.split(r"(?m)^---\s*$", manifest)
    deployments = 0
    for resource in resources:
        kind_match = re.search(r"(?m)^kind:\s*([A-Za-z]+)\s*$", resource)
        if not kind_match:
            continue
        kind = kind_match.group(1)
        if kind not in {"Deployment", "Service", "ConfigMap"}:
            continue
        deployments += kind == "Deployment"
        name_match = re.search(r"(?m)^metadata:\s*\{\s*name:\s*([A-Za-z0-9.-]+)", resource)
        if not name_match or name_match.group(1) != EXPECTED_DEPLOYMENT:
            errors.append(f"{kind} manifest must target only {EXPECTED_DEPLOYMENT}")
        if kind == "Deployment":
            images = re.findall(r"(?m)^\s*image:\s*([^\s]+)", resource)
            repositories = [image.rsplit("/", 1)[-1].rsplit(":", 1)[0] for image in images]
            if not repositories or any(repository != EXPECTED_REPOSITORY for repository in repositories):
                errors.append(f"Deployment image must come from ECR repository {EXPECTED_REPOSITORY}")
    if deployments != 1:
        errors.append(f"expected exactly one Deployment manifest, found {deployments}")
    return errors


def validate(project: Path = PROJECT) -> list[str]:
    errors: list[str] = []
    docs = project / "docs"
    for spec_id in SPEC_IDS:
        matches = sorted(docs.glob(f"{spec_id}-*.md"))
        presence_error = spec_presence_error(spec_id, len(matches))
        if presence_error:
            errors.append(presence_error)
            continue
        content = matches[0].read_text(encoding="utf-8")
        errors.extend(spec_content_errors(matches[0].name, spec_id, content))

    workflow_path = project / ".github" / "workflows" / "ci-cd.yml"
    spec10 = next(iter(docs.glob("SPEC-10-*.md")), None)
    if spec10 is not None and workflow_path.is_file():
        workflow = workflow_path.read_text(encoding="utf-8")
        ci_spec = spec10.read_text(encoding="utf-8")
        errors.extend(workflow_contract_errors(workflow, ci_spec))

    deployment_path = project / "k8s" / "deployment.yaml"
    if deployment_path.is_file():
        errors.extend(manifest_contract_errors(deployment_path.read_text(encoding="utf-8")))
    else:
        errors.append("missing k8s/deployment.yaml")

    if errors:
        return errors
    print(f"SPEC verification passed: {len(SPEC_IDS)} documents; CI gates and deploy target scoped to {EXPECTED_REPOSITORY}.")
    return []


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
