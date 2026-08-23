"""Offline tests for the Week 07 API client."""

import requests

from lab07_api_client import get_api_data


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


def test_api_client_returns_parsed_json(monkeypatch):
    payload = {"name": "snorlax", "weight": 4600}
    monkeypatch.setattr(
        requests,
        "get",
        lambda url, timeout: FakeResponse(payload=payload),
    )
    assert get_api_data("https://example.test/pokemon") == payload


def test_api_client_handles_http_errors(monkeypatch):
    error = requests.exceptions.HTTPError("404")
    monkeypatch.setattr(
        requests,
        "get",
        lambda url, timeout: FakeResponse(error=error),
    )
    assert get_api_data("https://example.test/missing") is None


def test_api_client_handles_network_errors(monkeypatch):
    def fail(url, timeout):
        raise requests.exceptions.ConnectionError("offline")

    monkeypatch.setattr(requests, "get", fail)
    assert get_api_data("https://example.test/offline") is None


def test_api_client_handles_invalid_json(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda url, timeout: FakeResponse(json_error=ValueError("invalid json")),
    )
    assert get_api_data("https://example.test/not-json") is None
