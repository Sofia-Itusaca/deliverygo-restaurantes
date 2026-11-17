# SPEC-01 — Descripción general, objetivos y alcance

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Definir DeliveryGo como catálogo web de seis restaurantes peruanos con consulta de menús servidos por dos APIs independientes.

## Alcance

Frontend con listado y detalle; Restaurant Service mantiene el catálogo; Menu Service entrega platos por UUID de restaurante. No incluye pedidos, carrito, autenticación ni pagos.

## Descripción técnica

SPA React/Vite con dos rutas. ASP.NET Core 10 + PostgreSQL y FastAPI + MongoDB. El frontend obtiene restaurantes de una API y menús de la otra. Los UUID deterministas 10000000-0000-4000-8000-000000000001…000006 enlazan los servicios.

## Requisitos relacionados

Requisitos 1–4, 7 y 12 de la solicitud DeliveryGo.

## Restricciones y estado

Sin usuarios, roles, login, carrito, pedidos, pagos, logística, administración ni bases compartidas.

## Criterios de aceptación

El listado muestra seis restaurantes obtenidos de Restaurant Service y el detalle consulta únicamente el menú asociado al UUID seleccionado.

## Evidencias y método de verificación

Listado con seis restaurantes; cada detalle consulta su restaurante y su propio menú.

## Especificaciones relacionadas

[SPEC-02](SPEC-02-arquitectura.md), [SPEC-03](SPEC-03-requisitos.md).
