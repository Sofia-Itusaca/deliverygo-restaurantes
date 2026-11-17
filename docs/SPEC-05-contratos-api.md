# SPEC-05 — Contratos API REST

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Describir rutas, payloads y errores públicos.

## Alcance

Restaurant Service: `GET /api/v1/restaurantes`, `GET /api/v1/restaurantes/{id}`. Menu Service: `GET /api/v1/menus/{restauranteId}`, `GET /api/v1/menus/{restauranteId}/{productoId}`. Ambos: `GET /health/live`, `GET /health/ready`.

## Descripción técnica

Restaurante JSON: id, nombre, descripcion, categoria, direccion, imagen_url, activo, fecha_creacion. Plato: id, restaurante_id, nombre, descripcion, categoria, precio, imagen_url, disponible. Precio es numérico en soles. Restaurant devuelve 404 para UUID inexistente; Menu valida UUID y devuelve 400 si inválido, 404 si plato no existe; fallos de almacenamiento se reportan como 503 en Menu y 500 genérico centralizado en Restaurant. Swagger `/swagger` y `/docs`.

## Requisitos relacionados

Requisitos 5 y 6.

## Restricciones y estado

CORS limita origen a `FrontendOrigin`/`FRONTEND_ORIGINS`, configurables. No hay autenticación.

## Criterios de aceptación

El listado de restaurantes devuelve seis registros; cada lista de menú contiene solo platos del UUID solicitado; la consulta individual devuelve el producto seleccionado y se respetan los códigos de error descritos.

## Evidencias y método de verificación

Smoke test consulta listados, platos, producto por ID, 404 de restaurante y health checks.

## Especificaciones relacionadas

[SPEC-02](SPEC-02-arquitectura.md), [SPEC-04](SPEC-04-bases-de-datos.md), [SPEC-06](SPEC-06-interfaz.md), [SPEC-13](SPEC-13-plan-de-pruebas.md).
