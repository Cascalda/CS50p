"""Tests fuel.py from pset_3."""

# pylint: disable=C0116
from fuel import convert, gauge
import pytest


def test_convert():
    test_pairs = (
        ("3/7", 43),
        ("3/4", 75),
        ("5/9", 56),
        ("0/41", 0),
        ("91/91", 100),
    )
    for fraction, answer in test_pairs:
        assert convert(fraction) == answer

    with pytest.raises(ZeroDivisionError):
        convert("51/0")

    with pytest.raises(ValueError):
        convert("431/110")


def test_gauge():
    test_pairs = (
        (0, "E"),
        (1, "E"),
        (99, "F"),
        (100, "F"),
        (45, "45%"),
        (98, "98%"),
    )
    for percentage, indicator in test_pairs:
        assert gauge(percentage) == indicator


if __name__ == "__main__":
    pytest.main()
