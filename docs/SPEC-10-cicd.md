# SPEC-10 — CI/CD y GitHub Actions

- **Versión:** 1.4.0
- **Estado:** vigente; actualizada al 2026-11-17
- **Historial:** 1.4.0 — 2026-11-17 — matriz de alternativas para GHSA-fc5q-39xc-vjpf; el fork hash-pinned mitiga solo los patrones probados, sin resolver los cinco HIGH del audit Node 22/npm 10.9.9; 1.3.0 — 2026-11-17 — prueba de regresión ReDoS y discrepancia de auditoría Node 22/Node 24; 1.2.0 — 2026-11-17 — auditorías de dependencias bloqueantes, Trivy estricto y gates Hadolint/Kubeconform; 1.1.0 — 2026-11-17 — SPEC gate, resumen de evidencias y despliegue manual opt-in; 1.0.0 — primera versión.

## Objetivo

Describir pipelines independientes, verificaciones y condición de publicación/despliegue.

## Alcance

Cada repo contiene `.github/workflows/ci-cd.yml`; CI y verificación estructural de sus 13 SPEC en push a main, pull request y ejecución manual. El job de despliegue requiere ejecución manual en main, `deploy_production=true` y variables/secretos de AWS revisados.

## Descripción técnica

Frontend: Python 3.12 valida SPEC-01..13 y contrato CI/deploy; npm ci, Vitest, auditorías de producción y completa bloqueantes, build, Hadolint, Kubeconform estricto, imagen y Trivy CRITICAL/HIGH exit 1 sin ignorar findings no corregibles. Un test de regresión acotado cubre `+(*a)`, `+(*)`, `*(*a)` y `+(a*b)`. El override hash-pinned comunitario mitiga los patrones probados, pero no es un release upstream corregido: se clasifican cero findings corregidos, una mitigación de casos específicos y cinco HIGH pendientes. Node 22/npm 10.9.9 reporta cinco HIGH; Node 24/npm 11.19.0 devuelve cero con el mismo lockfile, discrepancia que no se toma como resolución. La decisión transversal del Harness está documentada en `docs/picomatch-redos-decision.md` en la raíz del workspace; no se copia a los repositorios independientes. Restaurantes: SPEC gate, .NET 10 restore/build/xUnit, auditoría NuGet transitiva que falla ante HIGH/CRITICAL o severidad no clasificada, Hadolint, Kubeconform estricto, imagen y Trivy estricto. Menús: SPEC gate, pip install, pip-audit -r requirements.txt bloqueante, compileall, unittest, Ruff para errores críticos, Hadolint, Kubeconform estricto, imagen y Trivy estricto. Los tres Trivy gates usan CRITICAL/HIGH, exit 1 y no filtran findings no corregibles. Las auditorías de dependencias se ejecutan después de las verificaciones de build, imagen y Trivy, y corren con condición always cuando la restauración de dependencias pasó, para que un audit finding no omita tests, build ni escaneos. Los resúmenes Actions registran run, commit y gates. CD continúa limitado al dispatch manual, main, opt-in explícito, AWS_DEPLOY_ENABLED y ECR propio exacto; repositorios permitidos: deliverygo-frontend, deliverygo-restaurantes y deliverygo-menus. Aplica sólo recursos del componente mediante OIDC.

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
