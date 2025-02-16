from django.test import TestCase
from unrained.services.weather_service import new_weather_service, TemperatureUnit

class WeatherServiceTests(TestCase):
    
    def setUp(self):
        self.srv = new_weather_service()
    
    def test_convert_temperature(self):
        # K -> C
        self.assertEqual(self.srv.convert_temperature(273.15, TemperatureUnit.KELVIN, TemperatureUnit.CELSIUS), 0.0, "First one fucked")
        # C -> F
        self.assertEqual(self.srv.convert_temperature(0, TemperatureUnit.CELSIUS, TemperatureUnit.FAHRENHEIT), 32.0, "Second one fucked")
        # F -> K
        self.assertEqual(self.srv.convert_temperature(32, TemperatureUnit.FAHRENHEIT, TemperatureUnit.KELVIN), 273.15, "Third one fucked")
    
    def test_format_timezone_offset(self):
        self.assertEqual(self.srv.format_timezone_offset(3600), "+01:00")
        self.assertEqual(self.srv.format_timezone_offset(-7200), "-02:00")
    
    def test_temperature_status(self):
        self.assertEqual(self.srv.temperature_status(5), "Chilly")
        self.assertEqual(self.srv.temperature_status(15), "Mild")
        self.assertEqual(self.srv.temperature_status(25), "Warm")
        self.assertEqual(self.srv.temperature_status(35), "Hot")
        self.assertEqual(self.srv.temperature_status(45), "Roasting")
    
    def tearDown(self):
        pass