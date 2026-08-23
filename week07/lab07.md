# Lab 07: External data and APIs

**Due:** Sunday at 11:59 PM  
**Points:** 10

Work with JSON files and HTTP APIs while keeping tests deterministic and offline.

## Deliverables

Create:

- `week07/lab07_contact_book.py`
- `week07/lab07_api_client.py`

Do not modify the tests.

## Part 1: JSON contact book

Implement:

```python
def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""
```

Use a context manager for file access and `indent=4` when writing.

## Part 2: API client

Implement:

```python
def get_api_data(url):
    """Return parsed JSON from url, or None when the request or decoding fails."""
```

The function must:

- Call `requests.get(url, timeout=10)`
- Call `raise_for_status()`
- Return `response.json()` on success
- Return `None` for `requests.exceptions.RequestException` or invalid JSON

The tests replace `requests.get` with local fakes. They never contact a live service.

## Test locally

```bash
uv run --directory week07 python -m pytest tests/ -v
```

## Submit

```bash
git add week07/lab07_contact_book.py week07/lab07_api_client.py
git commit -m "Complete Lab 07"
git push origin main
```

A green Week 07 badge earns 10 points.
