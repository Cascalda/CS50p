"""Tests numb3rs.py."""
from numb3rs import validate
import pytest


# pylint: disable=missing-function-docstring
def test_valid():
    valid_cases = (r"127.0.0.1", r"8.8.8.8", r"12.12.120.102")
    for case in valid_cases:
        assert validate(case) is True


def test_invalid():
    invalid_cases = (r"256.0.0.123", r"12.34.56.789", r"1.1.1", r"123.-1.2.1")
    for case in invalid_cases:
        assert validate(case) is False


if __name__ == "__main__":
    pytest.main()
