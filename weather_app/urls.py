from django.urls import path
from . import views

# Try again

urlpatterns = [
    path("", views.city_search, name="city_search"),
    path("select/", views.city_selection, name="city_selection"),
]