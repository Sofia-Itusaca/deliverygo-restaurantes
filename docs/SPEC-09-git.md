# SPEC-09 — Organización Git y repositorios independientes

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Precisar separación y remotos de código.

## Alcance

FRONTEND → `Sofia-Itusaca/deliverygo-frontend`; SERVICIO 1 → `Sofia-Itusaca/deliverygo-restaurantes`; SERVICIO 2 → `Sofia-Itusaca/deliverygo-menus`.

## Descripción técnica

Cada carpeta tiene `.git` independiente, rama local `main` y `origin` HTTPS apuntando al repositorio correspondiente. Los archivos nuevos siguen sin commit; no se ha hecho push. Compose y arquitectura general están fuera de los repositorios.

## Requisitos relacionados

Requisitos 1 y 9.

## Restricciones y estado

Los cambios no se publican automáticamente. Cambios en un repo no disparan los pipelines de los otros.

## Criterios de aceptación

Cada carpeta conserva su propio `.git`, rama local `main` y remoto `origin` correspondiente; los workflows viven en el repo de su componente.

## Evidencias y método de verificación

`git status --short --branch` y `git remote -v` en cada carpeta; confirmar un `.git` por componente.

## Especificaciones relacionadas

[SPEC-10](SPEC-10-cicd.md).
