# SPEC-12 — AWS EKS y despliegue

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Registrar destino cloud previsto y dependencias aún pendientes.

## Alcance

Región objetivo `us-east-2`; workloads en EKS e imágenes en ECR; opciones de base PostgreSQL administrado y MongoDB Atlas.

## Descripción técnica

Workflow OIDC asume `AWS_ROLE_ARN`, login ECR, build/tag SHA/push, configura kubeconfig para `EKS_CLUSTER`, aplica namespace/deployment y espera rollout. `ECR_REPOSITORY` se define por repositorio. No hay valores de cuenta/ARN/cluster inventados.

## Requisitos relacionados

Requisitos 9–11.

## Restricciones y estado

No se crearon ni modificaron recursos AWS. Falta crear/configurar EKS, ECR, rol y trust OIDC least-privilege, secretos externos, conectividad privada de datos, origins y URLs API accesibles por navegador, Ingress y TLS/DNS.

## Criterios de aceptación

El job deploy requiere habilitación explícita y variables; sin ellas, CI no usa AWS.

## Evidencias y método de verificación

Pendiente: verificar identidad IAM, push ECR, acceso kubectl/RBAC, rollout y conectividad real de bases en entorno autorizado.

## Especificaciones relacionadas

[SPEC-10](SPEC-10-cicd.md), [SPEC-11](SPEC-11-kubernetes.md).
