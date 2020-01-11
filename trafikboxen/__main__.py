"""Entrypoint for the package"""
import os
from typing import Any

import requests

LUMA_STATION_ID = "1552"


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


def fetch_departures(station_id: str = "") -> Any:
    """
    Fetch departure information for a station
    :return: Departure information
    """
    pass


def display_departures(departures: Any) -> None:
    """
    Display the departures on screen.
    :param departures: Station departures
    :return: None
    """
    pass


def main():
    """
    Fetch  all station departure information and display it.
    :return:
    """
    pass


if __name__ == "__main__":
    print(fetch_sl_station_id("luma"))
