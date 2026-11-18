FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY *.csproj ./
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app/publish /p:UseAppHost=false
FROM mcr.microsoft.com/dotnet/aspnet:10.0
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl=8.5.0-2ubuntu10.16 && rm -rf /var/lib/apt/lists/*
ENV ASPNETCORE_URLS=http://+:8081 ASPNETCORE_ENVIRONMENT=Production
COPY --from=build /app/publish .
USER 1654
EXPOSE 8081
ENTRYPOINT ["dotnet","DeliveryGo.Restaurants.dll"]
