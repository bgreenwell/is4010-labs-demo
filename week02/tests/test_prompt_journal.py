"""Structural checks for the badge-graded Lab 02 comparison journal."""

from __future__ import annotations

import re
from pathlib import Path


JOURNAL = Path(__file__).parents[1] / "lab02_prompts.md"


# Markers left over from the template. "TODO" is matched case-sensitively and on word
# boundaries so that ordinary prose ("my todo list") does not fail the lab.
LEFTOVER_MARKERS = (
    re.compile(r"YOUR RESPONSE", re.IGNORECASE),
    re.compile(r"\[paste here\]", re.IGNORECASE),
    re.compile(r"\bTODO\b"),
)


def journal_text() -> str:
    assert JOURNAL.exists(), "Create week02/lab02_prompts.md from the template"
    text = JOURNAL.read_text(encoding="utf-8")
    for marker in LEFTOVER_MARKERS:
        assert not marker.search(text), (
            f"Replace every template marker in lab02_prompts.md (found {marker.pattern})"
        )
    return text


def section(text: str, heading: str, next_heading_level: int = 2) -> str:
    pattern = rf"(?ms)^{re.escape(heading)}\s*$\n(.*?)(?=^{'#' * next_heading_level}\s|\Z)"
    match = re.search(pattern, text)
    assert match, f"Missing required section: {heading}"
    return match.group(1).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def test_all_required_sections_exist():
    text = journal_text()
    headings = [
        "## Tool check",
        "### GitHub Copilot CLI",
        "### Antigravity CLI",
        "## Shared task",
        "### Shared prompt",
        "### Copilot CLI observations",
        "### Antigravity CLI observations",
        "### Comparison",
        "## Test-guided implementation",
        "## Preferred tool combination",
    ]
    for heading in headings:
        assert heading in text, f"Missing required heading: {heading}"

    prompt_blocks = re.findall(r"```text\s*\n(.+?)\n```", text, re.DOTALL)
    assert len(prompt_blocks) == 1, "Include one nonempty shared-prompt block"
    assert prompt_blocks[0].strip()


def test_tool_checks_are_completed():
    text = journal_text()
    tool_check = section(text, "## Tool check")
    assert word_count(tool_check) >= 20, "Complete both CLI tool checks"


def test_observations_and_comparison_have_required_length():
    text = journal_text()
    shared_task = section(text, "## Shared task")
    copilot = section(shared_task, "### Copilot CLI observations", 3)
    antigravity = section(shared_task, "### Antigravity CLI observations", 3)
    comparison = section(shared_task, "### Comparison", 3)
    assert word_count(copilot) >= 50
    assert word_count(antigravity) >= 50
    assert word_count(comparison) >= 100


def test_reflections_have_required_length():
    text = journal_text()
    implementation = section(text, "## Test-guided implementation")
    preference = section(text, "## Preferred tool combination")
    assert word_count(implementation) >= 100
    assert word_count(preference) >= 100
