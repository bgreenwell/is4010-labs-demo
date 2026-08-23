# Lab 05: Functions and error handling

**Due:** Sunday at 11:59 PM  
**Points:** 10

Refactor data-processing logic into small functions that handle missing and invalid values gracefully.

## Deliverable

Create `week05/lab05.py`. Do not copy or modify the provided tests.

## Functions

```python
def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
```

Requirements:

- A user is represented by a dictionary.
- Ignore missing ages and ages that are not numeric.
- Return `0.0` when there are no valid ages.
- Include an email only when `is_active` is truthy and the email key exists.
- Return an empty list when no active email addresses exist.
- Include clear docstrings.

## Test locally

```bash
uv run --directory week05 python -m pytest tests/ -v
```

## Submit

```bash
git add week05/lab05.py
git commit -m "Complete Lab 05"
git push origin main
```

A green Week 05 badge earns 10 points.
