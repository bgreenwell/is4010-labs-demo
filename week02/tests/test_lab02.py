"""Behavioral tests for Lab 02."""

from lab02 import count_vowels, is_even, make_greeting


def test_greeting_simple_name():
    assert make_greeting("Ada") == "Hello, Ada!"


def test_greeting_multiword_name():
    assert make_greeting("Grace Hopper") == "Hello, Grace Hopper!"


def test_greeting_empty_name():
    assert make_greeting("") == "Hello, !"


def test_even_positive_values():
    assert is_even(12) is True


def test_odd_positive_values():
    assert is_even(7) is False


def test_even_zero_and_negative_values():
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(-3) is False


def test_vowels_are_case_insensitive():
    assert count_vowels("OpenAI") == 4


def test_text_with_no_vowels():
    assert count_vowels("rhythms") == 0


def test_empty_text():
    assert count_vowels("") == 0
