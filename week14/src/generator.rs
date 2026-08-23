// Week 14: generator.rs
//
// Implement the three password generation functions below.
// Each function must produce output that satisfies the constraints in its docstring.
// The tests at the bottom verify your implementations.

#![allow(dead_code, unused_imports)]
use rand::Rng;

/// Generates a random password of the given `length`.
///
/// The character set is:
///   - Always included: lowercase letters (a–z), uppercase letters (A–Z), digits (0–9)
///   - Included when `use_symbols` is true: `!@#$%^&*`
///
/// Each character is chosen independently at random.
/// Panics if `length` is 0.
///
/// # Examples
/// ```
/// let pwd = generate_random(12, false);
/// assert_eq!(pwd.len(), 12);
/// ```
pub fn generate_random(_length: usize, _use_symbols: bool) -> String {
    todo!("Implement generate_random, hint: build a charset string then pick random chars from it using rand::thread_rng()")
}

/// Generates a passphrase made of `word_count` random common English words joined by `separator`.
///
/// Use the WORD_LIST constant defined below as your word source.
/// Each word is selected independently at random.
///
/// # Examples
/// ```
/// let phrase = generate_passphrase(3, '-');
/// // e.g. "apple-river-cloud"
/// assert_eq!(phrase.split('-').count(), 3);
/// ```
pub fn generate_passphrase(_word_count: usize, _separator: char) -> String {
    todo!("Implement generate_passphrase, hint: pick random indices into WORD_LIST, join with separator.to_string()")
}

/// Generates a numeric PIN of the given `length` (digits 0–9 only).
///
/// Panics if `length` is 0.
///
/// # Examples
/// ```
/// let pin = generate_pin(6);
/// assert_eq!(pin.len(), 6);
/// assert!(pin.chars().all(|c| c.is_ascii_digit()));
/// ```
pub fn generate_pin(_length: usize) -> String {
    todo!("Implement generate_pin, hint: sample from '0'..='9'")
}

// A small word list for passphrases.
pub const WORD_LIST: &[&str] = &[
    "apple", "river", "cloud", "stone", "flame", "ocean", "tiger", "maple", "storm", "frost",
    "eagle", "cedar", "brook", "ember", "coral", "prism", "solar", "lunar", "amber", "blaze",
    "cliff", "delta", "fable", "grove", "haven", "ivory", "jewel", "knoll", "lemon", "meadow",
    "north", "olive", "pearl", "quill", "ridge", "spark", "thorn", "umbra", "valor", "willow",
    "xenon", "yarrow", "zenith", "acorn", "birch", "crane", "drift", "elder", "flint", "glade",
    "hyena", "inlet", "junco", "kestrel",
];

// ============================================================================
// TESTS: DO NOT MODIFY
// ============================================================================
#[cfg(test)]
mod tests {
    use super::*;

    // --- generate_random ---

    #[test]
    fn test_random_correct_length() {
        let pwd = generate_random(12, false);
        assert_eq!(pwd.len(), 12);
    }

    #[test]
    fn test_random_no_symbols_only_alphanumeric() {
        let pwd = generate_random(100, false);
        assert!(
            pwd.chars().all(|c| c.is_ascii_alphanumeric()),
            "Password without symbols should only contain alphanumeric characters"
        );
    }

    #[test]
    fn test_random_with_symbols_contains_valid_chars() {
        let valid: std::collections::HashSet<char> =
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
                .chars()
                .collect();
        let pwd = generate_random(100, true);
        assert!(
            pwd.chars().all(|c| valid.contains(&c)),
            "Password with symbols must only contain chars from the allowed set"
        );
    }

    #[test]
    fn test_random_length_one() {
        let pwd = generate_random(1, false);
        assert_eq!(pwd.len(), 1);
    }

    #[test]
    #[should_panic]
    fn test_random_zero_length_panics() {
        generate_random(0, false);
    }

    // --- generate_passphrase ---

    #[test]
    fn test_passphrase_word_count() {
        let phrase = generate_passphrase(4, '-');
        assert_eq!(phrase.split('-').count(), 4);
    }

    #[test]
    fn test_passphrase_separator() {
        let phrase = generate_passphrase(3, '_');
        assert!(phrase.contains('_'));
        assert!(!phrase.contains('-'));
    }

    #[test]
    fn test_passphrase_words_from_list() {
        let phrase = generate_passphrase(5, '-');
        for word in phrase.split('-') {
            assert!(
                WORD_LIST.contains(&word),
                "Word '{}' is not in WORD_LIST",
                word
            );
        }
    }

    #[test]
    fn test_passphrase_single_word() {
        let phrase = generate_passphrase(1, '-');
        assert!(!phrase.contains('-'));
        assert!(WORD_LIST.contains(&phrase.as_str()));
    }

    // --- generate_pin ---

    #[test]
    fn test_pin_correct_length() {
        let pin = generate_pin(6);
        assert_eq!(pin.len(), 6);
    }

    #[test]
    fn test_pin_only_digits() {
        let pin = generate_pin(20);
        assert!(
            pin.chars().all(|c| c.is_ascii_digit()),
            "PIN must contain only digits"
        );
    }

    #[test]
    fn test_pin_length_one() {
        let pin = generate_pin(1);
        assert_eq!(pin.len(), 1);
        assert!(pin.chars().all(|c| c.is_ascii_digit()));
    }

    #[test]
    #[should_panic]
    fn test_pin_zero_length_panics() {
        generate_pin(0);
    }
}
