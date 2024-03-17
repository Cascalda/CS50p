"""Tests jar.py."""

from jar import Jar
import pytest

COOKIE_EMOJI = "🍪"
OVERFLOW_MODIFIER = 999


def test_init_sets_default_capacity():
    """Tests initialisation sets the correct default capacity."""
    jar = Jar()
    default_capacity = 12

    assert jar.capacity == default_capacity


def test_init_sets_custom_capacity():
    """Tests initialisation sets the correct custom capacity."""
    custom_capacity = 123
    jar = Jar(capacity=custom_capacity)

    assert jar.capacity == custom_capacity


def test_str_empty_jar():
    """Tests __str__ prints nothing in an empty jar."""
    jar = Jar()
    assert str(jar) == ""


def test_str_custom_size():
    """Tests __str__ prints out the correct representation of the jar size."""
    capacity = 40
    jar = Jar(capacity)

    size_value = 39
    jar.size = size_value

    assert str(jar) == (size_value * COOKIE_EMOJI)


def test_deposit():
    """Tests depositing cookies into the jar."""
    capacity = 60
    jar = Jar(capacity)

    deposit_value = 57
    jar.deposit(deposit_value)

    assert jar.size == deposit_value

    with pytest.raises(ValueError, match="Not enough capacity."):
        invalid_deposit = (capacity - deposit_value) + OVERFLOW_MODIFIER
        jar.deposit(invalid_deposit)


def test_withdraw():
    """Tests withdrawing cookies from the jar."""
    capacity = 21
    jar = Jar(capacity)

    size_value = 20
    jar.size = size_value

    withdrawal_value = 19
    jar.withdraw(withdrawal_value)

    assert jar.size == (size_value - withdrawal_value)

    with pytest.raises(ValueError, match="Not enough cookies to withdraw."):
        invalid_withdrawal = (capacity - withdrawal_value) + OVERFLOW_MODIFIER
        jar.withdraw(invalid_withdrawal)


if __name__ == "__main__":
    pytest.main()
