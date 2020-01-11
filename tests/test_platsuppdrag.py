from unittest import mock

from trafikboxen.platsuppslag import fetch_sl_station_id

mock_return_value = {
    "StatusCode": 0,
    "Message": None,
    "ExecutionTime": 0,
    "ResponseData": [
        {
            "Name": "The Fake Station",
            "SiteId": "1337",
            "Type": "Station",
            "X": "10000000",
            "Y": "10000000",
            "Products": None,
        },
    ],
}


@mock.patch("trafikboxen.platsuppslag.requests.get", autospec=True)
def test_fetch_sl_station_id(requests_mock):
    requests_mock.return_value.json.return_value = mock_return_value
    assert fetch_sl_station_id("fake_station") == "1337"
