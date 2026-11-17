# SPEC-07 — Docker y contenedores

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Describir imágenes y arranque local reproducible.

## Alcance

Cada repo tiene Dockerfile; Compose raíz define frontend, dos APIs, PostgreSQL y MongoDB.

## Descripción técnica

Frontend build Vite servido por Nginx unprivileged en 8080. Restaurant Service .NET 10 en 8081; Menu Service Python 3.12 en 8082. Bases sin puertos publicados, red bridge privada, health checks y volúmenes `postgres_data`/`mongo_data`. Compose espera health de DB y servicios. Variables de API Vite se fijan al build de imagen.

## Requisitos relacionados

Requisitos 8 y 12.

## Restricciones y estado

Variables de ejemplo/dummy locales no son secretos de producción. Para desarrollo frontend independiente Vite usa 5173; la imagen Compose sirve 8080.

## Criterios de aceptación

No ejecutar `down -v` si se desea conservar bases. Sin servicios externos obligatorios salvo descarga de imágenes/dependencias durante build.

## Evidencias y método de verificación

Compose debe iniciar los cinco componentes con DB privadas y volúmenes; frontend responde en 8080, APIs en 8081/8082 y ambas bases pasan sus health checks.

## Especificaciones relacionadas

[SPEC-02](SPEC-02-arquitectura.md), [SPEC-04](SPEC-04-bases-de-datos.md), [SPEC-08](SPEC-08-seguridad.md).
