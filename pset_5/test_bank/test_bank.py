"""Tests bank.py from pset_1."""

# pylint: disable=C0116
from bank import value
import pytest


def test_hello():
    hellos = ("hello", "Hello", "HeLlO")
    for hello in hellos:
        assert value(hello) == 0


def test_h_starter():
    h_starters = (
        "How's it going",
        "How's the weather?",
        "Hot innit?",
    )
    for h_starter in h_starters:
        assert value(h_starter) == 20


def test_others():
    others = (
        "What's up?",
        "Not bad",
        "Nothing much",
    )
    for other in others:
        assert value(other) == 100


if __name__ == "__main__":
    pytest.main()
