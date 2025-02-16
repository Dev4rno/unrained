import requests
from typing import Union
from handlers.env_handler import env
from enum import Enum, auto
import datetime as dt
from typing import List, Dict

class TemperatureUnit(Enum):
    CELSIUS = auto()  # °C
    FAHRENHEIT = auto()  # °F
    KELVIN = auto()  # K

class WeatherService:
    
    SEARCH_URL = "https://api.openweathermap.org/geo/1.0/direct"
    CITY_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self):
        api_key = env.app['api_key']
        self.city_url =  "?".join((self.CITY_URL, f"appid={api_key}"))
        self.search_url = "?".join((self.SEARCH_URL, f"appid={api_key}"))
        
    def find_cities(self, city_name: str, limit: int = 10) -> List[Dict]:
        """Fetch a list of cities matching the given name"""
        search_url = f"{self.search_url}&q={city_name}&limit={limit}"
        response = requests.get(search_url)
        response.raise_for_status()
        cities = response.json() 
        for city in cities:
            city["country"] = city["country"].lower()
        return cities

    def get_current_weather_by_location(self, lat: float, lon: float) -> dict:#, city: str):
        """Get weather for a given city"""
        city_url = "&".join((self.city_url, f"lat={lat}", f"lon={lon}"))
        weather = requests.get(city_url).json()
        main_data = weather["main"]
        main_data["temp"] = self.convert_temperature(main_data["temp"], TemperatureUnit.KELVIN, TemperatureUnit.CELSIUS)
        main_data["feels_like"] = self.convert_temperature(main_data["feels_like"], TemperatureUnit.KELVIN, TemperatureUnit.CELSIUS)
        main_data["temp_min"] = self.convert_temperature(main_data["temp_min"], TemperatureUnit.KELVIN, TemperatureUnit.CELSIUS)
        main_data["temp_max"] = self.convert_temperature(main_data["temp_max"], TemperatureUnit.KELVIN, TemperatureUnit.CELSIUS)
        weather["sys"]["sunrise"] = dt.datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime("%H:%M")
        weather["sys"]["sunset"] = dt.datetime.fromtimestamp(weather["sys"]["sunset"]).strftime("%H:%M")
        weather["sys"]["country"] = weather["sys"]["country"].lower()
        weather["timezone"] = self.format_timezone_offset(weather["timezone"])
        weather["status"] = self.temperature_status(main_data["temp"])
        return weather
    
    @staticmethod
    def convert_temperature(
        temperature: Union[float, int],
        from_unit: TemperatureUnit,
        to_unit: TemperatureUnit,
    ) -> float:
        """Convert temperature from one unit to another"""
        # Convert to Celsius first
        if from_unit == TemperatureUnit.CELSIUS:
            celsius = temperature
        elif from_unit == TemperatureUnit.FAHRENHEIT:
            celsius = (temperature - 32) * 5 / 9
        elif from_unit == TemperatureUnit.KELVIN:
            celsius = temperature - 273.15
        else:
            raise ValueError(f"Invalid 'from_unit': {from_unit}")
        # Celsius -> desired unit
        output = None
        if to_unit == TemperatureUnit.CELSIUS:
            output = celsius
        elif to_unit == TemperatureUnit.FAHRENHEIT:
            output = (celsius * 9 / 5) + 32
        elif to_unit == TemperatureUnit.KELVIN:
            output = celsius + 273.15
        else:
            raise ValueError(f"Invalid 'to_unit': {to_unit}")
        return round(output, 2)
    
    def temperature_status(self, temperature: float) -> str:
        """Returns humorous status message based on the temperature"""
        if temperature < -20:
            return "Arctic"
        elif -20 <= temperature < 0:
            return "Freezing"
        elif 0 <= temperature < 10:
            return "Chilly"
        elif 10 <= temperature < 20:
            return "Mild"
        elif 20 <= temperature < 30:
            return "Warm"
        elif 30 <= temperature < 40:
            return "Hot"
        elif 40 <= temperature < 50:
            return "Roasting"
        else:
            return "Hotter than the sun"
    
    @staticmethod
    def format_timezone_offset(timezone_offset: int) -> str:
        """Converts a timezone offset in seconds into a formatted string (e.g., +09:00)"""
        offset = dt.timedelta(seconds=timezone_offset)
        sign = "+" if offset >= dt.timedelta(0) else "-"
        total_seconds = abs(offset.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        timezone_str = f"{sign}{int(hours):02}:{int(minutes):02}"
        return timezone_str
    
def new_weather_service() -> WeatherService:
    return WeatherService()