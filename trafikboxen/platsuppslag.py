"""Package for interacting with the SL Platsuppslag API"""
import os

import requests


def fetch_sl_station_id(search_string: str) -> str:
    """
    Fetch an SL station ID based on a search string
    :param search_string: Search string
    :return: station ID
    """
    params = {
        "key": os.environ["PLATSUPPSLAG_API_KEY"],
        "SearchString": search_string,
    }
    res = requests.get("https://api.sl.se/api2/typeahead.json", params)
    return res.json()["ResponseData"][0]["SiteId"]
