//! Integration tests for the complete Week 14 command-line interface.

use std::process::{Command, Output};

fn run(args: &[&str]) -> Output {
    Command::new(env!("CARGO_BIN_EXE_week14"))
        .args(args)
        .output()
        .expect("the Week 14 binary should run")
}

fn stdout(output: &Output) -> String {
    assert!(
        output.status.success(),
        "command failed: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    String::from_utf8(output.stdout.clone()).expect("stdout should be UTF-8")
}

#[test]
fn random_command_prints_requested_length() {
    let text = stdout(&run(&["random", "--length", "20", "--symbols"]));
    let password = text
        .lines()
        .next()
        .and_then(|line| line.strip_prefix("Generated password: "))
        .expect("random command should print a generated password");
    assert_eq!(password.len(), 20);
    assert!(text.contains("Entropy:"));
}

#[test]
fn passphrase_command_prints_requested_words() {
    let text = stdout(&run(&["passphrase", "--words", "3", "--separator", "_"]));
    let phrase = text
        .trim()
        .strip_prefix("Generated passphrase: ")
        .expect("passphrase command should print a passphrase");
    assert_eq!(phrase.split('_').count(), 3);
}

#[test]
fn pin_command_prints_requested_digits() {
    let text = stdout(&run(&["pin", "--length", "8"]));
    let pin = text
        .trim()
        .strip_prefix("Generated PIN: ")
        .expect("pin command should print a PIN");
    assert_eq!(pin.len(), 8);
    assert!(pin.chars().all(|character| character.is_ascii_digit()));
}

#[test]
fn validate_command_prints_strength_and_entropy() {
    let text = stdout(&run(&["validate", "MyStr0ng!Pass2026"]));
    assert!(text.contains("Password strength:"));
    assert!(text.contains("Entropy:"));
}

#[test]
fn validate_command_warns_about_common_patterns() {
    let text = stdout(&run(&["validate", "password"]));
    assert!(text.contains("Warning:"));
}
