import unittest
import os
from dotenv import load_dotenv

load_dotenv()


class TestVarEnv(unittest.TestCase):
    def test_weather_api_key(self):
        owm_api_key = os.environ.get("OWM_API_KEY")
        self.assertIsNotNone(owm_api_key)

    def test_google_api_key(self):
        google_api_key = os.environ.get("GOOGLE_API_KEY")
        self.assertIsNotNone(google_api_key)

    def test_telegram_api_key(self):
        telegram_api_key = os.environ.get("TELEGRAM_API_KEY")
        self.assertIsNotNone(telegram_api_key)
