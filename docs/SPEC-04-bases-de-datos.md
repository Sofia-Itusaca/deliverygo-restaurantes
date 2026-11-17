# SPEC-04 — Diseño de bases de datos

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Especificar esquemas, identificadores e inicialización persistente.

## Alcance

PostgreSQL guarda restaurantes; MongoDB guarda documentos de menú. Volúmenes Compose conservan los datos.

## Descripción técnica

PostgreSQL `restaurantes`: id UUID PK, nombre, descripcion, categoria (POLLERIA/CHIFA, check constraint), direccion, imagen_url, activo, fecha_creacion. EF Core aplica migración inicial y seed completa UUIDs faltantes. Mongo `menus`: `_id` UUID determinista, restaurante_id, nombre, descripcion, categoria, precio positivo, imagen_url, disponible; índices por restaurante_id y compuesto (restaurante_id,_id). Seed usa upsert.

## Requisitos relacionados

Requisitos 5–7.

## Restricciones y estado

Las bases no son compartidas. Credenciales Compose son valores locales de demostración sustituibles por variables; `.env` real está ignorado.

## Criterios de aceptación

Las columnas/campos documentados concuerdan con las respuestas API; las dos bases contienen seis restaurantes correlacionados con cuatro documentos de menú por UUID y sus seeds no duplican datos al reiniciar las aplicaciones.

## Evidencias y método de verificación

Las bases no se comparten. No hay tablas/colecciones de usuarios, pedidos o pagos; credenciales locales de ejemplo no son para producción.

## Especificaciones relacionadas

[SPEC-02](SPEC-02-arquitectura.md), [SPEC-05](SPEC-05-contratos-api.md), [SPEC-07](SPEC-07-docker.md).
