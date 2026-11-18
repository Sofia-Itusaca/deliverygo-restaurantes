# SPEC-07 — Docker y contenedores

- **Versión:** 1.2.0
- **Estado:** vigente; actualizada al 2026-11-18
- **Historial:** 1.2.0 — 2026-11-18 — descripción sincronizada de imágenes y medidas por servicio: Nginx unprivileged, UID explícito y curl fijado para Restaurantes, Alpine actualizado y UID 10001 para Menús; 1.1.0 — endurecimiento de imagen Menu Service; 1.0.0 — primera versión.

## Objetivo

Describir imágenes y arranque local reproducible.

## Alcance

Cada repo tiene Dockerfile; Compose raíz define frontend, dos APIs, PostgreSQL y MongoDB.

## Descripción técnica

Cada repositorio construye solo su propia imagen. Frontend: Vite en Node 22 y Nginx unprivileged en 8080; `VITE_RESTAURANT_API_URL` y `VITE_MENU_API_URL` se incorporan al bundle durante `docker build`. Restaurantes: build multi-stage con .NET 10, runtime ASP.NET 10, `curl=8.5.0-2ubuntu10.16` para health checks, usuario no root UID 1654 y puerto 8081. Menús: `python:3.12-alpine`, `apk upgrade --no-cache` antes de instalar requirements, usuario no root UID 10001 y puerto 8082. Compose raíz define PostgreSQL y MongoDB sin puertos publicados, red bridge privada, health checks y volúmenes persistentes; cada repo conserva su Dockerfile y despliegue independiente.

## Requisitos relacionados

Requisitos 8 y 12.

## Restricciones

No publicar puertos de bases en Compose; no mezclar repositorios ni incluir secretos; cada CI construye solo su imagen.

## Criterios de aceptación

Las imágenes usan runtimes no privilegiados, exponen los puertos documentados y superan la construcción local/CI.

## Evidencias

`docker compose -f docker-compose.local.yml config --quiet`, `docker build` por repositorio y gates Docker de GitHub Actions.

## Especificaciones relacionadas

SPEC-02, SPEC-07, SPEC-10, SPEC-11 y SPEC-12.
