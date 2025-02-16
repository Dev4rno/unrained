from django.shortcuts import render, redirect
from handlers.env_handler import env
from services.sereno_service import new_sereno_service

srv = new_sereno_service()

def city_search(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name")
        cities = srv.find_cities(city_name)
        return render(request, "weather_app/city_selection.html", {"cities": cities[:3]})
    return render(request, "weather_app/city_search.html")

def city_selection(request):
    if request.method == "POST":
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")
        weather = srv.get_current_weather_by_location(lat, lon)
        return render(request, "weather_app/weather_result.html", {"weather": weather})
    return redirect("city_search")