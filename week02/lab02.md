# Lab 02: Compare CLI coding agents

**Due:** Sunday at 11:59 PM  
**Points:** 10

Formal Python instruction begins next week. In this lab, you will use two command-line coding agents as collaborators, compare their responses to the same small task, and use tests to decide what belongs in the repository. You are not expected to understand every Python construct yet.

## Learning objectives

By the end of this lab, you will be able to:

- Install and authenticate GitHub Copilot CLI and Antigravity CLI
- Run coding agents from inside a repository
- Compare two responses to the same prompt
- Use automated tests as independent evidence
- Inspect changes before committing them
- Choose a browser, editor, and CLI tool combination that fits your workflow

## 1. Install both CLI tools

Use the current official setup instructions rather than copied installer commands:

- [Install GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli)
- [Antigravity CLI overview](https://antigravity.google/docs/cli/overview/)

Authenticate each tool using its official flow. Never put a password, token, API key, or authentication output in this repository or your prompt journal.

## 2. Work from the repository

Open the cloned repository in VS Code and start its integrated terminal:

```bash
cd ~/is4010/is4010-labs
code .
git status
```

Launch each agent from this directory. An agent started here can inspect repository context, so stay inside the course repository and review every proposed command or edit.

## 3. Give both agents the same task

Copy `lab02_prompts.template.md` to `lab02_prompts.md`. Write one prompt for `count_vowels`, then submit that exact prompt to both Copilot CLI and Antigravity CLI. Record the shared prompt and your observations, but do not paste secrets or a full chat transcript.

The required Python contracts are:

```python
def make_greeting(name: str) -> str:
    """Return exactly 'Hello, NAME!' using the supplied name."""


def is_even(number: int) -> bool:
    """Return True when number is even and False otherwise."""


def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""
```

Create `week02/lab02.py` with all three functions. You may use either CLI, Copilot in VS Code, a browser chat, or your own reasoning for `make_greeting` and `is_even`. For `count_vowels`, compare the two CLI suggestions before choosing or combining an approach.

## 4. Test, inspect, and revise

Run the grader from the repository root:

```bash
uv run --directory week02 python -m pytest tests/ -v
git diff -- week02/lab02.py week02/lab02_prompts.md
```

If a test fails, give the agent the intended behavior and relevant failure message, then decide whether its revision is correct. Do not ask it merely to "make the tests pass." Inspect the final diff before committing it.

GitHub Actions checks the Python behavior and whether your journal has the required structure. It cannot verify which tools are installed on your computer; your journal is your record of completing the comparison.

## 5. Submit

```bash
git add week02/lab02.py week02/lab02_prompts.md
git commit -m "Complete Lab 02 CLI comparison"
git push origin main
```

A green Week 02 badge earns 10 points.
