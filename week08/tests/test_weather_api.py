"""Offline tests for the WeatherAPI client and formatters."""

import requests

from week08.weather_api import WeatherAPI, format_current_weather, format_forecast


class FakeResponse:
    def __init__(self, payload=None, error=None, json_error=None):
        self.payload = payload
        self.error = error
        self.json_error = json_error

    def raise_for_status(self):
        if self.error:
            raise self.error

    def json(self):
        if self.json_error:
            raise self.json_error
        return self.payload


def test_current_weather_request(monkeypatch):
    payload = {"location": {"name": "Cincinnati"}, "current": {"temp_f": 72}}
    observed = {}

    def fake_get(url, params, timeout):
        observed.update(url=url, params=params, timeout=timeout)
        return FakeResponse(payload=payload)

    monkeypatch.setattr(requests, "get", fake_get)
    client = WeatherAPI("secret")
    assert client.get_current_weather("Cincinnati") == payload
    assert observed["url"].endswith("/current.json")
    assert observed["params"] == {"key": "secret", "q": "Cincinnati"}
    assert observed["timeout"] == 10


def test_forecast_request_and_day_validation(monkeypatch):
    payload = {"forecast": {"forecastday": []}}
    observed = {}

    def fake_get(url, params, timeout):
        observed.update(url=url, params=params, timeout=timeout)
        return FakeResponse(payload=payload)

    monkeypatch.setattr(requests, "get", fake_get)
    client = WeatherAPI("secret")
    assert client.get_forecast("Paris", days=2) == payload
    assert observed["url"].endswith("/forecast.json")
    assert observed["params"]["days"] == 2

    for invalid in (0, 4):
        try:
            client.get_forecast("Paris", days=invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("days outside 1–3 must raise ValueError")


def test_requests_and_json_errors_return_none(monkeypatch):
    client = WeatherAPI("secret")

    def network_error(url, params, timeout):
        raise requests.exceptions.Timeout("slow")

    monkeypatch.setattr(requests, "get", network_error)
    assert client.get_current_weather("Nowhere") is None

    monkeypatch.setattr(
        requests,
        "get",
        lambda url, params, timeout: FakeResponse(json_error=ValueError("bad json")),
    )
    assert client.get_current_weather("Nowhere") is None


def test_format_current_weather():
    data = {
        "location": {"name": "Cincinnati", "country": "USA"},
        "current": {"temp_f": 72.5, "condition": {"text": "Sunny"}},
    }
    assert format_current_weather(data) == "Cincinnati, USA: 72.5°F, Sunny"


def test_format_forecast():
    data = {
        "forecast": {
            "forecastday": [
                {
                    "date": "2026-08-16",
                    "day": {
                        "maxtemp_f": 81,
                        "mintemp_f": 62,
                        "condition": {"text": "Partly cloudy"},
                    },
                }
            ]
        }
    }
    assert format_forecast(data) == "2026-08-16: high 81°F, low 62°F, Partly cloudy"
