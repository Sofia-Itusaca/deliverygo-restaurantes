import unittest

from verify_specs import (
    EXPECTED_REPOSITORY,
    REQUIRED_SECTIONS,
    WORKFLOW_GATES,
    manifest_contract_errors,
    spec_content_errors,
    spec_presence_error,
    workflow_contract_errors,
)


def valid_workflow():
    return "\n".join(WORKFLOW_GATES) + (
        "\npython scripts/verify_specs.py\n"
        "workflow_dispatch\ninputs.deploy_production == true\n"
        "  deploy:\n"
        "    if: github.event_name == 'workflow_dispatch' && inputs.deploy_production == true "
        "&& vars.AWS_DEPLOY_ENABLED == 'true' "
        f"&& vars.ECR_REPOSITORY == '{EXPECTED_REPOSITORY}'\n"
        "    run: aws eks update-kubeconfig && kubectl apply -f k8s/namespace.yaml -f k8s/deployment.yaml -n deliverygo\n"
    )


def valid_spec(spec_id):
    sections = "\n".join(f"## {section}\ntexto" for section in REQUIRED_SECTIONS)
    return f"# {spec_id}\n{sections}\n{EXPECTED_REPOSITORY if spec_id == 'SPEC-10' else ''}"


class VerifySpecsTests(unittest.TestCase):
    def test_accepts_complete_spec_with_accented_headings(self):
        self.assertEqual([], spec_content_errors("SPEC-10.md", "SPEC-10", valid_spec("SPEC-10")))

    def test_rejects_missing_spec(self):
        self.assertEqual("expected exactly one SPEC-06, found 0", spec_presence_error("SPEC-06", 0))

    def test_rejects_missing_required_section(self):
        content = valid_spec("SPEC-03").replace("## Objetivo\ntexto", "")
        self.assertTrue(any("Objetivo" in error for error in spec_content_errors("SPEC-03.md", "SPEC-03", content)))

    def test_accepts_workflow_with_gates_manual_opt_in_and_own_target(self):
        self.assertEqual([], workflow_contract_errors(valid_workflow(), EXPECTED_REPOSITORY))

    def test_rejects_other_service_target_and_missing_manual_opt_in(self):
        workflow = valid_workflow().replace("inputs.deploy_production == true", "false")
        workflow = workflow.replace(f"vars.ECR_REPOSITORY == '{EXPECTED_REPOSITORY}'", "vars.ECR_REPOSITORY == 'other-service'")
        workflow = workflow.replace(f"deployment/{EXPECTED_REPOSITORY}", "deployment/other-service")
        errors = workflow_contract_errors(workflow, EXPECTED_REPOSITORY)
        self.assertTrue(any("manual dispatch" in error for error in errors))
        self.assertTrue(any("scoped" in error or "exact ECR_REPOSITORY" in error for error in errors))

    def test_rejects_manifest_with_another_service_deployment(self):
        manifest = "kind: Deployment\nmetadata: {name: other-service}\n"
        self.assertTrue(any("must target only" in error for error in manifest_contract_errors(manifest)))

    def test_rejects_foreign_service_image(self):
        manifest = (
            "kind: Deployment\nmetadata: {name: " + EXPECTED_REPOSITORY + "}\n"
            "spec:\n  containers:\n    - image: registry/deliverygo-menus:latest\n"
        )
        self.assertTrue(any("Deployment image" in error for error in manifest_contract_errors(manifest)))


if __name__ == "__main__":
    unittest.main()
