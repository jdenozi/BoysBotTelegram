import datetime
import unittest

from src.database import Database


class TestDatabase(unittest.TestCase):
    def test_create_database(self):
        database = Database()
        self.assertIsNotNone(database)

    def test_get_event_db(self):
        database = Database()
        event_db = database.get_event_db()
        self.assertIsNotNone(event_db)

    def test_add_new_event_planning(self):
        database = Database()
        date = datetime.date(2021, 9, 21)
        resp = database.add_new_event_planning("julien_test", "test", "this is a test", date)
        self.assertEqual(resp, True)
        res = database.search_event_planning_by_title("test")
        self.assertIsNotNone(res)
        res = database.drop_event_planning_by_title("test")
        self.assertTrue(res)

