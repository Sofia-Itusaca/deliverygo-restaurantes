# SPEC-03 — Requisitos funcionales y no funcionales

- **Versión:** 1.0.0
- **Estado:** vigente; describe la implementación local al 2026-11-17
- **Historial:** 1.0.0 — 2026-11-17 — primera versión, alineada con el código del workspace.

## Objetivo

Registrar comportamientos verificables y cualidades de la aplicación.

## Alcance

RF: catálogo de seis restaurantes, búsqueda por nombre, filtros Pollerías/Chifas, detalle y platos/precio/disponibilidad. RNF: responsive, APIs con health checks, datos persistentes y validación.

## Descripción técnica

Frontend implementa dos páginas y estados de carga, error y vacío. Restaurant API filtra activos. Menú contiene cuatro platos por restaurante: las tres porciones obligatorias de pollo más papas, y cuatro platos propios de chifa.

## Requisitos relacionados

Secciones 2–7 y 12 de la solicitud.

## Restricciones y estado

Precios demo en S/; valores no representan oferta comercial. Imágenes y tipografías se descargan de Unsplash/Google Fonts. No hay carrito ni acción de compra; las API, y no arreglos frontend, son fuente de datos.

## Criterios de aceptación

El home presenta seis restaurantes desde API; búsqueda y filtros reducen resultados correctamente. El detalle muestra los platos propios con foto, descripción, disponibilidad y precio en soles, y el layout se adapta a viewport móvil.

## Evidencias y método de verificación

Pruebas frontend verifican seis cards, filtros, búsqueda y navegación; integración verifica menús y API.

## Especificaciones relacionadas

[SPEC-01](SPEC-01-descripcion-general.md), [SPEC-05](SPEC-05-contratos-api.md), [SPEC-06](SPEC-06-interfaz.md), [SPEC-13](SPEC-13-plan-de-pruebas.md).
