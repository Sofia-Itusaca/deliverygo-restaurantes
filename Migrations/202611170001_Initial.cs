using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using DeliveryGo.Restaurants;
[DbContext(typeof(RestaurantDb))]
[Migration("202611170001_Initial")]
public sealed class Initial : Migration
{
    protected override void Up(MigrationBuilder m)
    {
        m.CreateTable(name:"restaurantes",columns:t=>new { id=t.Column<Guid>(type:"uuid",nullable:false), nombre=t.Column<string>(type:"character varying(140)",maxLength:140,nullable:false), descripcion=t.Column<string>(type:"character varying(500)",maxLength:500,nullable:false), categoria=t.Column<string>(type:"character varying(20)",maxLength:20,nullable:false), direccion=t.Column<string>(type:"character varying(180)",maxLength:180,nullable:false), imagen_url=t.Column<string>(type:"character varying(500)",maxLength:500,nullable:false), activo=t.Column<bool>(type:"boolean",nullable:false), fecha_creacion=t.Column<DateTime>(type:"timestamp with time zone",nullable:false)},constraints:t=>{t.PrimaryKey("pk_restaurantes",x=>x.id);t.CheckConstraint("ck_restaurantes_categoria","categoria IN ('POLLERIA','CHIFA')");});
    }
    protected override void Down(MigrationBuilder m)=>m.DropTable("restaurantes");
}
