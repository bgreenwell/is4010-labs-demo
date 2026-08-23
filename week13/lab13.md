# Lab 13: Idiomatic Rust

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs` and implement every `todo!()`. The test suite is pre-written, so make it pass. Do not modify the test module.

When implementing a function, rename parameters by dropping the leading `_`.

## What to implement

**Part 1: iterators and closures**

| Function | Description |
|----------|-------------|
| `analyze_text(text)` | Return `(word_count, avg_word_length, longest_word)`; use iterator adaptors |
| `process_numbers(numbers)` | Sum of squares of all even numbers: `[1,2,3,4]` → `4+16 = 20` |
| `make_counter()` | Return a closure (`impl FnMut() -> i32`) that increments on each call |

For `make_counter`: the closure wrapper is already in place, so rename `_count` to `count`, increment it, and return the new value.

**Part 2: error handling with `Result`**

| Function / type | Description |
|-----------------|-------------|
| `divide(a, b)` | `Ok(a / b)` or `Err("division by zero")` when `b == 0.0` |
| `Display for ParseError` | Both variants must produce a non-empty message |
| `parse_positive_number(input)` | Parse `input` as `i32 > 0`; return `ParseError::NotANumber` or `ParseError::NotPositive` on failure |

## Test locally

Run these from the `week13` directory:

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

CI runs `cargo fmt --check`, so run `cargo fmt` before you push.

## Submit

```bash
git add week13/
git commit -m "Complete Lab 13"
git push origin main
```

A green Week 13 badge earns 10 points.
