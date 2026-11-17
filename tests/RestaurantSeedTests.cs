using DeliveryGo.Restaurants;
using Microsoft.EntityFrameworkCore;
using Xunit;

public class RestaurantSeedTests
{
    [Fact]
    public async Task Seed_is_repeatable_and_keeps_the_six_stable_restaurants()
    {
        var options = new DbContextOptionsBuilder<RestaurantDb>()
            .UseInMemoryDatabase(Guid.NewGuid().ToString())
            .Options;
        await using var db = new RestaurantDb(options);
        await RestaurantSeed.SeedAsync(db);
        await RestaurantSeed.SeedAsync(db);
        var all = await db.Restaurants.OrderBy(x => x.Nombre).ToListAsync();
        Assert.Equal(6, all.Count);
        Assert.Equal(3, all.Count(x => x.Categoria == "POLLERIA"));
        Assert.Equal(3, all.Count(x => x.Categoria == "CHIFA"));
        Assert.Equal(Guid.Parse("10000000-0000-4000-8000-000000000001"), all.Single(x => x.Nombre == "Pollería El Buen Sabor").Id);
    }
}
