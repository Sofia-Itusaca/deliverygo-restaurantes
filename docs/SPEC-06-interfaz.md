# SPEC-06 — Diseño de interfaz y navegación

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Documentar las dos pantallas y reglas visuales implementadas.

## Alcance

Página inicial con seis restaurantes en grilla de tres columnas en escritorio; detalle separado por ruta `/restaurantes/:id`.

## Descripción técnica

Paleta: naranja #E96D2C, vino #4B1110, verde #9DBB4D, fondo #F7F7F2, gris #ECEDEA, texto #26332F. Tarjetas muestran imagen, nombre, categoría, descripción y link. Home tiene búsqueda y filtros; detalle muestra foto, dirección, menú, descripción, disponibilidad y precio S/. CSS aplica breakpoints. Datos llegan de las APIs.

## Requisitos relacionados

Requisitos 2–4.

## Restricciones y estado

Las imágenes Unsplash y Google Fonts requieren acceso externo; no hay assets inventados como archivos locales.

## Criterios de aceptación

En escritorio se muestran tres tarjetas por fila y seis en total; búsqueda y filtros funcionan, detalle se abre en ruta independiente y las fotos/precios pertenecen al restaurante seleccionado.

## Evidencias y método de verificación

Vitest/jsdom comprueba seis cards, filtros, búsqueda y acceso a detalle; CSS define adaptación móvil.

## Especificaciones relacionadas

[SPEC-03](SPEC-03-requisitos.md), [SPEC-05](SPEC-05-contratos-api.md), [SPEC-13](SPEC-13-plan-de-pruebas.md).
