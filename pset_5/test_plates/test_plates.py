"""Tests plates.py from pset_2."""
from plates import is_valid
import pytest

test_data = [
    (
        "alphabet",
        [
            (True, ["CS501", "VS41", "VG2321"]),  # Valid cases
            (False, ["F350", "50GA68"]),  # Invalid cases
        ],
    ),
    (
        "length",
        [
            (True, ["ABC1", "LK505", "YHBAS2", "VABH45"]),
            (False, ["", "AB0", "ABCDEF1"]),
        ],
    ),
    (
        "special characters",
        [
            (True, ["RTG1", "GVT421", "TR42"]),
            (False, ["PO@50", "AV./45", "AS%1"]),
        ],
    ),
    (
        "numbers",
        [
            (True, ["YU10", "RTL125", "TPL108"]),
            (False, ["PO0798", "AA101A", "ABC0"]),
        ],
    ),
]


@pytest.mark.parametrize(
    "expected_result, value",
    (
        (expected_result, value)
        for _, cases in test_data  # Discard the category
        for expected_result, values in cases
        for value in values
    ),
)
def test_validation_categorized(expected_result, value):
    """Test validation function with categorized test cases."""
    assert is_valid(value) is expected_result


if __name__ == "__main__":
    pytest.main()
