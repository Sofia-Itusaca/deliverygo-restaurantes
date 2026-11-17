# DeliveryGo Restaurant Service

ASP.NET Core Web API para consultar el catálogo persistido de seis restaurantes.

## Especificaciones

Consulta la [documentación técnica y funcional](docs/README.md) (SPEC-01 a SPEC-13).

ASP.NET Core 10 Web API + EF Core + PostgreSQL. Requiere .NET 10 y PostgreSQL. Configura `ConnectionStrings__Restaurants` con el ejemplo de `.env.example` y ejecuta `dotnet run --urls http://localhost:8081`.

Swagger: `/swagger`. Endpoints: `GET /api/v1/restaurantes`, `GET /api/v1/restaurantes/{id}`, `/health/live`, `/health/ready`. La inicialización migra el esquema e inserta seis UUID estables de manera idempotente.

Pruebas unitarias de la semilla: `dotnet test tests/DeliveryGo.Restaurants.Tests.csproj -c Release`. Para comprobar PostgreSQL y las dos API en conjunto desde la carpeta principal: `python integration_smoke.py` con Compose iniciado.
