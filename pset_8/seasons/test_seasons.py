"""Tests seasons.py."""

from seasons import convert_age_to_words
import pytest

testcases = [
    ("26541", "Twenty-six thousand, five hundred forty-one minutes"),
    ("12345", "Twelve thousand, three hundred forty-five minutes"),
    ("1010101", "One million, ten thousand, one hundred one minutes"),
    ("66666", "Sixty-six thousand, six hundred sixty-six minutes"),
]


@pytest.mark.parametrize("input_text, expected_result", testcases)
def test_convert_age_to_words(input_text, expected_result):
    """Test convert_age_to_words function."""
    assert convert_age_to_words(input_text) == expected_result


if __name__ == "__main__":
    pytest.main()
