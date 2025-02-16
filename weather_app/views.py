from django.shortcuts import render, redirect
from handlers.env_handler import env
from services.weather_service import new_weather_service

srv = new_weather_service()

def city_search(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name")
        cities = srv.find_cities(city_name)
        if len(cities) == 0:
            return redirect("/")
        return render(request, "weather_app/city_selection.html", {"cities": cities[:3]})
    return render(request, "weather_app/city_search.html")

def city_selection(request):
    if request.method == "POST":
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")
        weather = srv.get_current_weather_by_location(lat, lon)
        return render(request, "weather_app/weather_result.html", {"weather": weather})
    return redirect("/")