"""Tests twttr.py from pset_2."""

# pylint: disable=C0116
from twttr import shorten
import pytest


def test_empty_input():
    assert shorten("") == ""


def test_no_vowels():
    no_vowels = "cyst Dryly	ply fly	Lynch gypsy	Myths Spy Crypt	Myths slyly"
    assert shorten(no_vowels) == no_vowels


def test_only_vowels():
    all_vowels = "aEeAiUoIuO"
    assert shorten(all_vowels) == ""


def test_jumbled_vowels():
    jumbled_vowels = "Already encyclopedia Indigo Oppenheimer undone"
    assert shorten(jumbled_vowels) == "lrdy ncyclpd ndg ppnhmr ndn"


def test_only_special_char():
    only_special_char = ",./?!"
    assert shorten(only_special_char) == only_special_char


def test_only_numbers():
    only_numbers = "1029384756"
    assert shorten(only_numbers) == only_numbers


if __name__ == "__main__":
    pytest.main()
