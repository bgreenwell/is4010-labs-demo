"""Command-level tests for the Week 08 weather CLI."""

from week08 import weather


class FakeWeatherAPI:
    def __init__(self, api_key):
        assert api_key == "test-key"

    def get_current_weather(self, location):
        return {
            "location": {"name": location, "country": "USA"},
            "current": {"temp_f": 70, "condition": {"text": "Clear"}},
        }

    def get_forecast(self, location, days=3):
        return {
            "forecast": {
                "forecastday": [
                    {
                        "date": "2026-08-16",
                        "day": {
                            "maxtemp_f": 80,
                            "mintemp_f": 60,
                            "condition": {"text": "Clear"},
                        },
                    }
                ]
            }
        }


def configure_cli(monkeypatch, tmp_path):
    monkeypatch.setattr(weather, "WeatherAPI", FakeWeatherAPI)
    monkeypatch.setattr(weather, "load_api_key", lambda: "test-key")
    monkeypatch.setattr(weather, "FAVORITES_FILE", tmp_path / "favorites.json")


def test_parser_exposes_all_commands():
    parser = weather.build_parser()
    assert parser.parse_args(["current", "Cincinnati"]).command == "current"
    assert parser.parse_args(["forecast", "Paris", "--days", "2"]).days == 2
    assert parser.parse_args(["favorites", "list"]).favorites_command == "list"


def test_favorites_add_list_and_remove(monkeypatch, tmp_path, capsys):
    configure_cli(monkeypatch, tmp_path)
    assert weather.main(["favorites", "add", "home", "Cincinnati, OH"]) == 0
    assert weather.main(["favorites", "list"]) == 0
    assert "home: Cincinnati, OH" in capsys.readouterr().out
    assert weather.main(["favorites", "remove", "home"]) == 0


def test_current_weather_uses_favorite(monkeypatch, tmp_path, capsys):
    configure_cli(monkeypatch, tmp_path)
    weather.main(["favorites", "add", "home", "Cincinnati"])
    capsys.readouterr()
    assert weather.main(["current", "home"]) == 0
    assert "Cincinnati, USA: 70°F, Clear" in capsys.readouterr().out


def test_forecast_command(monkeypatch, tmp_path, capsys):
    configure_cli(monkeypatch, tmp_path)
    assert weather.main(["forecast", "Paris", "--days", "2"]) == 0
    assert "2026-08-16: high 80°F, low 60°F, Clear" in capsys.readouterr().out


def test_missing_api_key_returns_failure(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(weather, "load_api_key", lambda: None)
    monkeypatch.setattr(weather, "FAVORITES_FILE", tmp_path / "favorites.json")
    assert weather.main(["current", "Cincinnati"]) == 1
    assert "API key" in capsys.readouterr().err
