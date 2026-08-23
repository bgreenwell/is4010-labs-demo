# Lab 10: Ownership and borrowing

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs`. There are two parts.

**Part 1, borrow-checker puzzles (not graded automatically):** Seven functions are commented out with `/* ... */`. Each has a compile error. Read the comment above each one, fix the broken code, then uncomment the call in `main()` to verify it runs.

**Part 2, implementation exercises (graded):** Implement the four `pub` functions below. Remove the leading `_` from parameter names as you go. Do not modify the test module.

## What to implement (Part 2)

| Function | Signature | Description |
|----------|-----------|-------------|
| `to_uppercase_owned` | `(s: String) -> String` | Take ownership, convert to uppercase, return |
| `string_length` | `(s: &String) -> usize` | Borrow immutably, return length |
| `append_suffix` | `(s: &mut String, suffix: &str)` | Mutably borrow, append `suffix` in place |
| `concat_strings` | `(s1: &str, s2: &str) -> String` | Borrow two slices, return a new owned `String` |

## Test locally

Run these from the `week10` directory:

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

CI runs `cargo fmt --check`, so run `cargo fmt` before you push.

## Submit

```bash
git add week10/
git commit -m "Complete Lab 10"
git push origin main
```

A green Week 10 badge earns 10 points.
