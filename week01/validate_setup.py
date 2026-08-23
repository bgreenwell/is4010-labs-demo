"""Validate the machine-readable fields in the Lab 01 setup record."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


SETUP_PATH = Path(__file__).with_name("student_setup.md")


def field(text: str, label: str) -> str:
    """Return the backtick-delimited value for a labeled Markdown field."""
    match = re.search(rf"^- {re.escape(label)}: `([^`]+)`$", text, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing field: {label}")
    return match.group(1).strip()


def main() -> int:
    """Validate the student's setup record against the GitHub repository."""
    if not SETUP_PATH.exists():
        print("Missing week01/student_setup.md. Copy and edit the template.")
        return 1

    text = SETUP_PATH.read_text(encoding="utf-8")
    try:
        username = field(text, "GitHub username")
        fork_url = field(text, "Fork URL")
        clone_verified = field(text, "Local clone verified").lower()
        uv_version = field(text, "uv version")
        python_version = field(text, "Python version")
    except ValueError as error:
        print(error)
        return 1

    owner = os.environ.get("GITHUB_REPOSITORY_OWNER", username)
    expected_url = f"https://github.com/{owner}/is4010-labs"
    errors: list[str] = []

    if username != owner:
        errors.append(f"GitHub username must match the fork owner: {owner}")
    if fork_url.rstrip("/") != expected_url:
        errors.append(f"Fork URL must be {expected_url}")
    if clone_verified != "yes":
        errors.append("Local clone verified must be `yes`")

    if not re.fullmatch(r"\d+\.\d+\.\d+", uv_version):
        errors.append("uv version must use the format `0.x.x`")

    version_match = re.fullmatch(r"(\d+)\.(\d+)(?:\.\d+)?", python_version)
    if not version_match or tuple(map(int, version_match.groups()))[:2] != (3, 12):
        errors.append("Python version must be the course version, Python 3.12")

    placeholders = ("YOUR-USERNAME", "yes-or-no", "0.x.x", "3.12.x")
    if any(placeholder in text for placeholder in placeholders):
        errors.append("Replace every template placeholder")

    if errors:
        for error in errors:
            print(f"- {error}")
        return 1

    print("Lab 01 setup record is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
