# IS4010 labs

This repository contains all 14 labs for **IS4010: AI-enhanced application development**. Labs 01–08 use the Python development environment; Labs 09–14 use Rust.

> [!NOTE]
> **This is a demonstration repository, not the course repository.**
>
> It shows what your fork's badges look like partway through the semester:
>
> - **Week 01 is green.** The setup record was pushed and passed every check.
> - **Week 02 is red.** The code has a bug, and the prompt journal was never created.
>   Select the badge to read the failure.
> - **Weeks 03 to 14 have no status.** Those workflows have not run yet, which is what a
>   badge looks like before you have pushed anything for that week.
>
> Fork [bgreenwell/is4010-labs](https://github.com/bgreenwell/is4010-labs) for your own work.

> [!WARNING]
> Work only in the files identified by each lab. Do not modify this README, lab instructions, tests, or anything under `.github/`. Those files control automated grading.

## Lab status

A green badge on your fork's `main` branch means the corresponding lab is complete and earns **10 points**.

| Lab | Topic | Status |
|---:|---|:---:|
| 01 | Repository and development setup | [![Week 01](../../actions/workflows/week01.yml/badge.svg?branch=main)](../../actions/workflows/week01.yml) |
| 02 | Compare CLI coding agents | [![Week 02](../../actions/workflows/week02.yml/badge.svg?branch=main)](../../actions/workflows/week02.yml) |
| 03 | Python basics and automated testing | [![Week 03](../../actions/workflows/week03.yml/badge.svg?branch=main)](../../actions/workflows/week03.yml) |
| 04 | Data structures | [![Week 04](../../actions/workflows/week04.yml/badge.svg?branch=main)](../../actions/workflows/week04.yml) |
| 05 | Functions and error handling | [![Week 05](../../actions/workflows/week05.yml/badge.svg?branch=main)](../../actions/workflows/week05.yml) |
| 06 | Object-oriented programming | [![Week 06](../../actions/workflows/week06.yml/badge.svg?branch=main)](../../actions/workflows/week06.yml) |
| 07 | External data and APIs | [![Week 07](../../actions/workflows/week07.yml/badge.svg?branch=main)](../../actions/workflows/week07.yml) |
| 08 | Weather CLI application | [![Week 08](../../actions/workflows/week08.yml/badge.svg?branch=main)](../../actions/workflows/week08.yml) |
| 09 | Rust basics | [![Week 09](../../actions/workflows/week09.yml/badge.svg?branch=main)](../../actions/workflows/week09.yml) |
| 10 | Ownership and borrowing | [![Week 10](../../actions/workflows/week10.yml/badge.svg?branch=main)](../../actions/workflows/week10.yml) |
| 11 | Structs, enums, and methods | [![Week 11](../../actions/workflows/week11.yml/badge.svg?branch=main)](../../actions/workflows/week11.yml) |
| 12 | Generics and traits | [![Week 12](../../actions/workflows/week12.yml/badge.svg?branch=main)](../../actions/workflows/week12.yml) |
| 13 | Idiomatic Rust | [![Week 13](../../actions/workflows/week13.yml/badge.svg?branch=main)](../../actions/workflows/week13.yml) |
| 14 | CLI application | [![Week 14](../../actions/workflows/week14.yml/badge.svg?branch=main)](../../actions/workflows/week14.yml) |

## Start here

Complete [Lab 01](week01/lab01.md). It walks you through the terminal, forking this repository, cloning your fork, enabling GitHub Actions, and preparing Python with `uv` for the first half of the course.

GitHub disables workflows in a new public fork until its owner enables them. Open the **Actions** tab in your fork and select **I understand my workflows, go ahead and enable them** before pushing your Lab 01 setup record.

## Weekly workflow

1. Read `weekXX/labXX.md`.
2. Work only in the files the lab identifies.
3. Run the week's checks locally until they pass.
4. Commit and push to your fork's `main` branch.
5. Confirm that the corresponding badge above is green.

## Python labs (weeks 02-08)

Set up the environment once, and again whenever `uv.lock` changes:

```bash
uv sync --locked
```

Run a week's tests from the repository root:

```bash
uv run --directory week03 python -m pytest tests/ -v
```

Week 08 is the exception; it runs from the root without `--directory`:

```bash
uv run python -m pytest week08/tests/ -v
```

There is one check here: the tests. A failure tells you almost everything you need. It names the
test, shows the line that failed, and prints what it expected against what your code returned:

```
>       assert get_list_of_even_numbers([-4, -3, -2, 0, 1, 2]) == [-4, -2, 0, 2]
E       assert [2] == [-4, -2, 0, 2]
E         At index 0 diff: 2 != -4
```

That output says the function dropped the zero and the negative evens. Read it before you change
anything. A useful prompt here is "this test expects `[-4, -2, 0, 2]` but my function returns
`[2]`; what condition am I applying that I should not be?"

## Rust labs (weeks 09-14)

Run all three from inside the week's directory:

```bash
cd week09
cargo test
cargo fmt
cargo clippy -- -D warnings
```

Rust labs have **three** checks, not one: correctness, formatting, and lints. CI runs all three,
so code that passes every test can still leave the badge red. That is not a trick. Formatting and
lints are part of ordinary Rust work, and clippy is worth reading: it explains the idiom rather
than just rejecting your code.

Most of it fixes itself:

```bash
cargo clippy --fix --allow-dirty
cargo fmt
```

One common lint is **not** auto-fixable, and it comes straight from Python habits:

| Clippy says | Rewrite |
|---|---|
| `the loop variable i is only used to index` | `for n in numbers` instead of `for i in 0..numbers.len()` |

Clippy names the file, the line, and the lint, and links to an explanation:

```
error: the loop variable `i` is only used to index `numbers`
   --> src/main.rs:150:14
    |
150 |     for i in 0..numbers.len() {
    |              ^^^^^^^^^^^^^^^^
```

Paste that whole block when you ask for help, including the `-->` line and any `help:` or `note:`
lines. The compiler's borrow-checker errors are worth the same treatment; they are unusually
detailed and an assistant can work directly from them.

## Working with your AI assistant

The failure output above is exactly the context an assistant needs, so the checks are where these
tools earn their keep.

- **Start the agent inside your clone** so it can read the lab, your code, and the test file.
- **Paste the whole failure, not a summary.** `pytest` and `cargo` both name the file, the line,
  and the reason. Trimming that away removes what makes the answer accurate.
- **Ask what the check expects and why your code differs**, rather than "make the tests pass."
  The second kind of prompt tends to produce code that satisfies the check without fixing the
  misunderstanding, and you still have to explain what you submitted.
- **Never paste an API key, token, or credential** into a prompt. This matters from week 08 on.
- **You are responsible for every line you submit.** Read the explanation, make the change
  yourself, and re-run the check locally before you push.
- **If your assistant proposes editing a test, a workflow, or a lab file, stop.** Those files set
  your grade, and `AGENTS.md` in this repository tells agents they are read-only. A test that was
  changed to pass is a false green badge, not a finished lab. Inspect `git diff` before every
  commit so you always know what changed.

Environment problems, such as a tool that will not install or a workflow that never ran, are
covered in the [course troubleshooting guide](https://bgreenwell.github.io/is4010-website/resources/troubleshooting.html).
