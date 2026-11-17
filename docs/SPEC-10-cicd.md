# SPEC-10 — CI/CD y GitHub Actions

- **Versión:** 1.1.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.1.0 — 2026-11-17 — SPEC gate en CI, resumen de evidencias y despliegue manual opt-in limitado al ECR/Deployment propio; 1.0.0 — primera versión.

## Objetivo

Describir pipelines independientes, verificaciones y condición de publicación/despliegue.

## Alcance

Cada repo contiene `.github/workflows/ci-cd.yml`; CI y verificación estructural de sus 13 SPEC en push a main, pull request y ejecución manual. El job de despliegue requiere ejecución manual en main, `deploy_production=true` y variables/secretos de AWS revisados.

## Descripción técnica

Frontend: Python 3.12 valida SPEC-01..13 y el contrato CI/deploy; npm ci, Vitest, npm audit, build y build/Trivy de imagen. Restaurant: el mismo gate de SPEC, setup .NET 10, restore, build, xUnit, imagen y Trivy. Menu: el mismo gate de SPEC, pip install, compileall, unittest, Ruff para errores críticos, imagen y Trivy. Resumen de GitHub Actions registra run, commit y resultado de gates. CD solo tras dispatch manual con `deploy_production=true`, en main, `AWS_DEPLOY_ENABLED=true`, EKS y el `ECR_REPOSITORY` exacto del componente. Mapeo de repositorios/destinos: frontend `deliverygo-frontend` → `Deployment/deliverygo-frontend`; restaurantes `deliverygo-restaurantes` → `Deployment/deliverygo-restaurantes`; menús `deliverygo-menus` → `Deployment/deliverygo-menus`. Asume rol con OIDC, aplica solo los recursos locales del componente (Deployment, Service y ConfigMap) y espera el rollout de su Deployment.

## Requisitos relacionados

Requisitos 9–11.

## Restricciones y estado

AWS_ROLE_ARN y confianza OIDC deben configurarse en GitHub/AWS; ECR y EKS deben existir. Los pipelines no crean recursos cloud. CI detecta SPEC faltantes/incompletas y drift entre gates de esta SPEC y el workflow; no prueba automáticamente contradicciones semánticas entre prosa y código, que requieren tests de contrato/revisión. Scans GitHub no se han ejecutado desde este workspace.

## Criterios de aceptación

CI no depende de AWS. CD queda omitido en push/PR y dispatch por defecto; solo se habilita con opt-in manual, variable AWS y destino ECR propio exacto.

## Evidencias y método de verificación

Inspección de YAML y ejecución local equivalente de pruebas/build; resultado remoto CI pendiente hasta publicar repos.

## Especificaciones relacionadas

[SPEC-08](SPEC-08-seguridad.md), [SPEC-09](SPEC-09-git.md), [SPEC-11](SPEC-11-kubernetes.md), [SPEC-12](SPEC-12-aws-eks.md).
