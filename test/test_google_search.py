import unittest
from src.google_search import google_search_first_result


class TestGoogleSearch(unittest.TestCase):
    def test_search(self):
        res = google_search_first_result("Café", num=1)
        print(res)
