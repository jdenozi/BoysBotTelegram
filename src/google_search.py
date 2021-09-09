import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


def google_search_first_result(search_term: str, num: int = 1) -> dict:
    """
    Search on Google with the search term given. Return a json.
    :param num: Number of results
    :param search_term: String content of the term
    :return: Json containing result of the search term
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    cse_id = os.environ.get("CSE_ID")
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, num=num).execute()
    return res
