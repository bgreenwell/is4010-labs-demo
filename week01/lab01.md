# Lab 01: Repository and development setup

**Due:** Sunday at 11:59 PM  
**Points:** 10

This lab prepares the single repository you will use for every lab in the course. You will use the terminal, fork the repository, clone your fork, prepare the course Python environment with `uv`, enable GitHub Actions, and push a short setup record. Rust is already included for later in the semester; you will install its toolchain before Week 09.

## Learning objectives

By the end of this lab, you will be able to:

- Navigate folders and run commands in a terminal
- Explain the difference between a repository, fork, and clone
- Configure Git with your identity
- Fork and clone a GitHub repository
- Verify that your local `origin` points to your fork
- Create the course Python environment with `uv`
- Enable and inspect GitHub Actions
- Commit and push a change to GitHub

## 1. Install the Week 01 tools

Follow the course [setup guide](https://bgreenwell.github.io/is4010-website/resources/setup.html) and the official documentation it links to. Install:

- Visual Studio Code
- Git
- `uv`

Use Git Bash on Windows, which the Git installer put there for you, or your default shell on macOS/Linux. Open a terminal directly or choose **Terminal > New Terminal** in VS Code, then verify:

```bash
code --version
git --version
uv --version
```

## 2. Practice the terminal basics

A command runs in your current working directory. Practice these commands before continuing:

```bash
pwd
ls
mkdir -p ~/is4010
cd ~/is4010
pwd
code .
```

Use Tab to complete paths, the Up arrow to reuse a command, and Ctrl+C to stop a running command. Read commands before pressing Enter, especially commands suggested by an AI assistant.

## 3. Configure Git

```bash
git config --global user.name "Your name"
git config --global user.email "your-email@example.com"
git config --global --list
```

Use the email associated with your GitHub account. Follow GitHub's current authentication instructions when prompted; never paste a token into a file or commit it.

## 4. Fork the semester repository

1. Open <https://github.com/bgreenwell/is4010-labs>.
2. Select **Fork**.
3. Keep the repository name `is4010-labs`.
4. Create the fork under your own GitHub account.

Your fork URL should look like:

```text
https://github.com/YOUR-USERNAME/is4010-labs
```

## 5. Clone your fork

```bash
cd ~/is4010
git clone https://github.com/YOUR-USERNAME/is4010-labs.git
cd is4010-labs
git remote -v
```

Both `origin` lines must contain your GitHub username. If they point to `bgreenwell`, you cloned the course repository instead of your fork.

## 6. Prepare Python with uv

From the repository root, run:

```bash
uv sync --locked
uv run python --version
uv run python -m pytest --version
```

`uv` reads `.python-version`, creates the local `.venv`, and installs the exact dependencies in `uv.lock`. You do not need to activate the environment or install Python separately.

## 7. Enable GitHub Actions

Open the **Actions** tab in your fork. If GitHub displays a warning that workflows are disabled, select **I understand my workflows, go ahead and enable them**.

## 8. Create your setup record

Copy the template and edit the copy:

```bash
cp week01/student_setup.template.md week01/student_setup.md
```

Replace every placeholder. Record the exact versions printed by `uv --version` and `uv run python --version`, and mark local clone verification as `yes`.

## 9. Commit and push

```bash
git add week01/student_setup.md
git commit -m "Complete Lab 01 setup"
git push origin main
```

Open your fork's README and wait for the Week 01 badge to turn green. Select the badge to inspect the workflow if it fails.

## Submit on Canvas

Submit this single URL:

```text
https://github.com/YOUR-USERNAME/is4010-labs
```

A green Week 01 badge earns 10 points.
