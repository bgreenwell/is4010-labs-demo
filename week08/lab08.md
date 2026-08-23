# Lab 08: Weather CLI application

**Due:** Sunday at 11:59 PM  
**Points:** 10

Build a complete command-line weather application combining HTTP requests, classes, JSON persistence, formatting, and `argparse`. Automated tests use fake responses; no API key or live network connection is used in grading.

## Deliverables

Create:

- `week08/favorites.py`
- `week08/weather_api.py`
- `week08/weather.py`

The supplied `config.example.py`, tests, workflow, and root `.gitignore` must not be modified. For manual use, copy `config.example.py` to the ignored `config.py` and add your own key there.

## Favorites manager

Implement `FavoritesManager(filename)` with:

- `add(name, location)`
- `remove(name)`
- `list_all()`
- `get_location(name)`

Names are case-insensitive. Save data as JSON after changes. Missing or corrupted files must produce an empty collection.

## Weather API client

Implement:

```python
class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"): ...
    def get_current_weather(self, location): ...
    def get_forecast(self, location, days=3): ...


def format_current_weather(data): ...
def format_forecast(data): ...
```

Requirements:

- Use `requests.get(..., params=..., timeout=10)`.
- Use the `current.json` and `forecast.json` endpoints.
- Return `None` for request or JSON errors.
- Raise `ValueError` when forecast days are outside 1–3.
- Format current weather as `CITY, COUNTRY: TEMP°F, CONDITION`.
- Format each forecast day as `DATE: high TEMP°F, low TEMP°F, CONDITION`.

## Command-line interface

In `weather.py`, expose:

```python
def load_api_key(): ...
def build_parser(): ...
def main(argv=None) -> int: ...
```

Support:

```bash
python week08/weather.py current LOCATION
python week08/weather.py forecast LOCATION --days 2
python week08/weather.py favorites add NAME LOCATION
python week08/weather.py favorites list
python week08/weather.py favorites remove NAME
```

A favorite name can replace a location in `current` and `forecast`. Return exit status 0 on success and 1 for missing keys, failed requests, duplicate additions, or missing removals. Send errors to standard error.

Load the API key from the `WEATHER_API_KEY` environment variable first, then from the ignored local `config.py`.

## Test locally

```bash
uv run python -m pytest week08/tests/ -v
```

## Manual API setup

```bash
cp week08/config.example.py week08/config.py
# Edit config.py and replace the placeholder.
python week08/weather.py current Cincinnati
```

Never commit `config.py` or an API key.

## Submit

```bash
git add week08/favorites.py week08/weather_api.py week08/weather.py
git commit -m "Complete Lab 08"
git push origin main
```

A green Week 08 badge earns 10 points.
