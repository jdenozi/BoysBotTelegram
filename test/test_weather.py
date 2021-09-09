import unittest

from src.weather import get_weather

ERROR_CITY_NAME = "Je suis désolé, je ne connais pas le nom de votre ville"


class TestWeather(unittest.TestCase):

    def test_get_weather(self):
        response = get_weather("Nimes")
        self.assertIsNotNone(response)

    def test_get_weather_without_real_city_name(self):
        response = get_weather("")
        self.assertIsNotNone(response)
        self.assertEqual(response, ERROR_CITY_NAME)
