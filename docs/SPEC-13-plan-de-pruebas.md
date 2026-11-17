# SPEC-13 — Plan de pruebas y criterios de aceptación

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Definir pruebas manuales/automatizadas y distinguir evidencia observada de verificaciones pendientes.

## Alcance

Frontend Vitest; pruebas unitarias de seed .NET y validaciones Python; smoke HTTP integrado; build de imágenes y Compose.

## Descripción técnica

Comandos: `npm test`, `npm run build`; `dotnet test tests/DeliveryGo.Restaurants.Tests.csproj -c Release`; en contenedor Menu `python -m unittest discover -s tests -v`; en raíz `python integration_smoke.py`. Aceptación integra exactamente seis restaurantes, 4 platos/restaurante, platos requeridos, aislamiento, lookup, 404 y readiness.

## Requisitos relacionados

Requisito 12 y criterios de las SPEC-03/05/06.

## Restricciones y estado

Evidencia registrada el 2026-11-17 en workspace local: Vitest 2/2; Restaurant xUnit 1/1; Menu unittest 3/3; integración seis restaurantes/24 platos y health OK; build frontend y .NET OK; Compose levantó DB y servicios saludables, frontend HTTP 200 y los datos siguieron disponibles tras recrear los servicios de aplicación. No se reiniciaron los contenedores DB para verificar persistencia a través de ese reinicio; esta prueba queda pendiente. No se afirma prueba de navegador real, GitHub Actions, Trivy remoto ni EKS.

## Criterios de aceptación

La suite cubre filtros/búsqueda/navegación, seed repetible y validación de UUID/precio; smoke de integración confirma seis restaurantes, menús aislados y health correcto en Compose. Las pruebas cloud/seguridad y visuales en dispositivos reales quedan fuera de esta aceptación local.

## Evidencias y método de verificación

Repetir comandos anteriores; para despliegue, sumar pruebas de conectividad DNS/TLS y rollout en AWS configurado.

## Especificaciones relacionadas

[SPEC-03](SPEC-03-requisitos.md), [SPEC-05](SPEC-05-contratos-api.md), [SPEC-06](SPEC-06-interfaz.md).
