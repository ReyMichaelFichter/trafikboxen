"""Entrypoint for the package"""
import os
from typing import Any

import requests

from trafikboxen.platsuppslag import fetch_sl_station_id

LUMA_STATION_ID = "1552"


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
