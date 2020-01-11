"""Entrypoint for the package"""
from time import sleep
from typing import Any


def fetch_departures(station: Any) -> Any:
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
    while True:
        main()
        sleep(15)
