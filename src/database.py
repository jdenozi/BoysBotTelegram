import json
from datetime import date
import pymongo

EVENT_DATABASE_NAME = "event"
EVENT_PLANNING_DATABASE_NAME = "event_planning"

DATE_FORMAT = "%d %b %Y "
ERROR_ADD_NEW_EVENT = "Error add new event"
MONGO_HOST = "mongodb://localhost:27017/"


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_HOST)
        self.event = self.client[("%s" % EVENT_DATABASE_NAME)]
        self.event_planning = self.event[("%s_planning" % EVENT_PLANNING_DATABASE_NAME)]

    def get_event_db(self):
        return self.event

    def get_event_planning_db(self):
        return self.event_planning

    def add_new_event_planning(self, author: str, event_title: str, event_description: str, event_date: date) -> bool:
        """
        Insert new event in event database
        :param author: Name of the person who create the event
        :param event_title
        :param event_description: Description of the event
        :param event_date: Date of the event
        :return True if the the insertion of new event is successfully work.
        """
        new_event = {
            "author": author,
            "creation_date": date.today().strftime(DATE_FORMAT),
            "event_title": event_title,
            "event_date": event_date.strftime(DATE_FORMAT),
            "event_description": event_description
        }
        try:
            if self.check_presence_event_planning(event_title):
                self.get_event_planning_db().insert_one(new_event)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            print("%s" % ERROR_ADD_NEW_EVENT)
            return False

    def search_event_planning_by_title(self, event_title: str) -> json:
        """
        Search event by event title
        :param event_title: Title of the event
        :return: The information of None Is the title doesn't exist
        """
        for item in self.get_event_planning_db().find():
            if item["event_title"] == event_title:
                return item
        return None

    def drop_event_planning_by_title(self, title_event: str) -> bool:
        """
        Remove document on event planning database by title
        :param title_event: the name of the event
        :return: True if the remove is successfully done
        """
        resp = self.search_event_planning_by_title(title_event)
        id_resp = resp["_id"]
        if resp is not None:
            self.event_planning.delete_one({"_id": id_resp})
            return True
        else:
            return False

    def check_presence_event_planning(self, title_event: str) -> bool:
        """
        Check if the title event is already use in the data base
        :param title_event: Title of the event
        :return: False if it's already use
        """
        resp = self.search_event_planning_by_title(title_event)
        if resp is not None:
            return False
        return True
