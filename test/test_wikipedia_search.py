import unittest
import wikipedia

from src.wikipedia_search import search_on_wikipedia


class TestWikipediaSearch(unittest.TestCase):
    def test_search_on_wikipedia(self):
        res = search_on_wikipedia("café")
        self.assertIsNotNone(res)

    def test_search_on_wikipedia_without_good_keyword(self):
        res = search_on_wikipedia("sdlkqd")
        self.assertIs(type(res), wikipedia.exceptions.PageError)
