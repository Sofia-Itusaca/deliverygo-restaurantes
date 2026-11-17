# SPEC-08 — Seguridad y restricciones

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Registrar controles implementados y brechas de preparación.

## Alcance

Separación de datos y secretos locales, exposición de servicios y contenedores.

## Descripción técnica

`.env` excluido; ejemplos sin credenciales reales de producción. DB sin puertos host. APIs validan UUID/categoría/precio; errores no filtran excepciones. Imágenes runtime ejecutan sin root (Nginx unprivileged, usuarios Docker Python/.NET). K8s manifiestos fijan non-root, capabilities drop, read-only FS donde procede, límites y probes. GitHub OIDC se configura con AWS_ROLE_ARN.

## Requisitos relacionados

Requisitos 8–11.

## Restricciones y estado

No JWT/login. Password Compose por defecto es demostrativo. K8s necesita Secret externo `deliverygo-db` y rol IAM restringido. Las NetworkPolicies y RBAC explícitos aún no están implementados; Deployment usa service account por defecto. ECR/EKS no configurados.

## Criterios de aceptación

No almacenar secretos reales ni habilitar despliegue AWS sin infraestructura y rol de confianza revisados.

## Evidencias y método de verificación

No hay secretos reales en Git, bases no publican puertos host y las imágenes de aplicación usan usuarios no privilegiados; CI contiene análisis Trivy. La revisión de Trivy en GitHub y la configuración IAM real son pendientes.

## Especificaciones relacionadas

[SPEC-07](SPEC-07-docker.md), [SPEC-10](SPEC-10-cicd.md), [SPEC-11](SPEC-11-kubernetes.md), [SPEC-12](SPEC-12-aws-eks.md).
