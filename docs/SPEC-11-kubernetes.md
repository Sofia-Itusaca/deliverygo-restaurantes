# SPEC-11 — Kubernetes

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Documentar recursos propios de cada componente.

## Alcance

Cada `k8s/` contiene namespace `deliverygo`, Deployment, Service ClusterIP y ConfigMap.

## Descripción técnica

Dos réplicas; probes HTTP readiness/liveness; requests/limits. Frontend Nginx port 8080 con usuario no root/read-only y volúmenes temporales para runtime. APIs escuchan 8081/8082, non-root, capabilities drop. Menús y restaurantes toman URL DB de Secret externo `deliverygo-db`; ConfigMaps mantienen configuración no sensible. Imágenes ECR tienen marcadores reemplazados por workflow.

## Requisitos relacionados

Requisitos 10 y 11.

## Restricciones y estado

No se incluyen manifiestos para PostgreSQL/MongoDB, Secret con datos, Ingress, DNS/TLS, NetworkPolicy o RBAC explícito. Servicios son ClusterIP y requieren entrada/API pública definida fuera para acceso desde navegador.

## Criterios de aceptación

Cada componente define su Namespace, Deployment, Service y ConfigMap; API espera Secret de base externa, y las imágenes placeholder se sustituyen en el job CD. Los servicios API quedan aislados como ClusterIP.

## Evidencias y método de verificación

Revisión estática y `kubectl apply`/rollout pendientes de clúster configurado.

## Especificaciones relacionadas

[SPEC-08](SPEC-08-seguridad.md), [SPEC-10](SPEC-10-cicd.md), [SPEC-12](SPEC-12-aws-eks.md).
