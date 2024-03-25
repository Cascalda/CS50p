"""Tests working.py."""

# pylint: disable=C0116
from working import convert
import pytest

valid_cases = [
    ("9 AM to 5 PM", "09:00 to 17:00"),
    ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
    ("8 PM to 8 AM", "20:00 to 08:00"),
    ("8:00 PM to 8:00 AM", "20:00 to 08:00"),
    ("12 AM to 12 PM", "00:00 to 12:00"),
    ("12:00 AM to 12:00 PM", "00:00 to 12:00"),
]

invalid_cases = [
    (
        ValueError,
        [
            "8:60 AM to 4:60 PM",
            "9AM to 5PM",
            "09:00 to 17:00",
            "9 AM - 5 PM",
            "10:7 AM - 5:1 PM",
        ],
    ),
]


@pytest.mark.parametrize("testcase, expected_result", valid_cases)
def test_valid_cases(testcase, expected_result):
    assert convert(testcase) == expected_result


@pytest.mark.parametrize("expected_exception, testcases", invalid_cases)
def test_invalid_cases(expected_exception, testcases):
    for testcase in testcases:
        with pytest.raises(expected_exception):
            convert(testcase)


if __name__ == "__main__":
    pytest.main()
