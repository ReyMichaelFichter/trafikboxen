from unittest import mock

from trafikboxen.platsuppslag import fetch_sl_station_id

mock_return_value = {
    "StopLocation": [
        {
            "id": "740024928",
            "extId": "740024928",
            "name": "Stockholm Mårtensdal",
            "lon": 18.088103,
            "lat": 59.302692,
            "weight": 2656,
            "products": 192,
        }
    ]
}


@mock.patch("trafikboxen.platsuppslag.requests.get", autospec=True)
def test_fetch_sl_station_id(requests_mock):
    requests_mock.return_value.json.return_value = mock_return_value
    assert fetch_sl_station_id("fake_station") == "740024928"
