# SPEC-02 — Arquitectura de microservicios

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Documentar los componentes y sus límites.

## Alcance

Describe frontend, servicios, bases separadas y flujos HTTP, tanto en Compose como en una futura instalación EKS.

## Descripción técnica

Frontend ejecuta requests REST desde el navegador. Restaurant Service accede solo a PostgreSQL; Menu Service accede solo a MongoDB. Compose comunica servicios por DNS interno; el navegador local usa puertos publicados 8081/8082. No hay gateway.

## Requisitos relacionados

Requisitos 4–7.

## Restricciones y estado

IDs UUID estables compartidos como valor contractual; entidades y persistencia no se comparten. Cada servicio tiene Dockerfile y pipeline separados.

## Criterios de aceptación

El navegador consume ambas API; Restaurant Service accede solo a PostgreSQL y Menu Service accede solo a MongoDB, cada uno desplegable y construible por separado.

## Evidencias y método de verificación

Las tres carpetas son aplicaciones/repositorios separados y cada API puede construirse por separado.

## Especificaciones relacionadas

[SPEC-01](SPEC-01-descripcion-general.md), [SPEC-04](SPEC-04-bases-de-datos.md), [SPEC-05](SPEC-05-contratos-api.md), [SPEC-07](SPEC-07-docker.md).
