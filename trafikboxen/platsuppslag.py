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
        "input": search_string,
        "format": "json",
    }
    res = requests.get("https://api.resrobot.se/v2/location.name", params)
    return res.json()["StopLocation"][0]["id"]
