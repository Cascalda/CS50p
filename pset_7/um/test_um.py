"""Tests um.py."""
from um import count
import pytest

testcases = [
    ("um", 1),
    ("Um um um", 3),
    ("omg umm can you um", 1),
    ("uM", 1),
]


@pytest.mark.parametrize("input_text, expected_result", testcases)
def test_count(input_text: str, expected_result: int) -> None:
    """Test count function."""
    assert count(input_text) == expected_result


if __name__ == "__main__":
    pytest.main()
