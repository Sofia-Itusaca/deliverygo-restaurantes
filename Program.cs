using DeliveryGo.Restaurants;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Diagnostics.HealthChecks;
using System.Text.Json;
var builder=WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<RestaurantDb>(o=>o.UseNpgsql(builder.Configuration.GetConnectionString("Restaurants")??"Host=localhost;Port=5432;Database=deliverygo;Username=deliverygo;Password=deliverygo_local"));
builder.Services.AddCors(o=>o.AddDefaultPolicy(p=>p.WithOrigins((builder.Configuration["FrontendOrigin"]??"http://localhost:5173").Split(',')).AllowAnyHeader().AllowAnyMethod()));
builder.Services.AddHealthChecks().AddNpgSql(builder.Configuration.GetConnectionString("Restaurants")??"Host=localhost;Port=5432;Database=deliverygo;Username=deliverygo;Password=deliverygo_local",name:"postgres",tags:new[]{"ready"});builder.Services.AddEndpointsApiExplorer();builder.Services.AddSwaggerGen();
var app=builder.Build();app.Use(async(ctx,next)=>{try{await next();}catch(Exception ex){app.Logger.LogError(ex,"Unhandled request error");ctx.Response.StatusCode=500;ctx.Response.ContentType="application/json";await ctx.Response.WriteAsync(JsonSerializer.Serialize(new{error="Ocurrió un error interno."}));}});app.UseCors();app.UseSwagger();app.UseSwaggerUI();
app.MapGet("/health/live",()=>Results.Ok(new{status="healthy"}));app.MapHealthChecks("/health/ready",new HealthCheckOptions{Predicate=c=>c.Tags.Contains("ready")});
var api=app.MapGroup("/api/v1/restaurantes");api.MapGet("/",async(RestaurantDb db)=>Results.Ok(await db.Restaurants.AsNoTracking().Where(r=>r.Activo).OrderBy(r=>r.Nombre).ToListAsync()));api.MapGet("/{id:guid}",async(Guid id,RestaurantDb db)=>await db.Restaurants.AsNoTracking().FirstOrDefaultAsync(r=>r.Id==id&&r.Activo) is { } r?Results.Ok(r):Results.NotFound(new{error="Restaurante no encontrado."}));
await using(var scope=app.Services.CreateAsyncScope()){var db=scope.ServiceProvider.GetRequiredService<RestaurantDb>();var attempts=0;while(true){try{await db.Database.MigrateAsync();await RestaurantSeed.SeedAsync(db);break;}catch(Exception ex) when(attempts++<25){app.Logger.LogWarning(ex,"Database unavailable; retrying");await Task.Delay(TimeSpan.FromSeconds(2));}}}
app.Run();
