"""Convert ISO 8601 formatted dates to words."""


def main() -> None:
    """Interface to control all other functions."""
    Jar()


class Jar:
    """A class representing a jar with a given capacity."""

    def __init__(self, capacity=12):
        """Initialise the string with a given capacity."""
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """Returns a string representatio of a jar."""
        return self._size * "🍪"

    def deposit(self, to_deposit: int) -> None:
        """Deposit cookies into the jar."""
        if (self._size + to_deposit) > self._capacity:
            raise ValueError("Not enough capacity.")

        self._size += to_deposit

    def withdraw(self, to_withdraw: int) -> None:
        """Withdraw cookies from the jar."""
        if self._size < to_withdraw:
            raise ValueError("Not enough cookies to withdraw.")

        self._size -= to_withdraw

    @property
    def capacity(self) -> int:
        """Get the capacity of the jar."""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity_value: int) -> None:
        if not (isinstance(capacity_value, int) or capacity_value < 0):
            raise ValueError("Capacity must be a non_negative integer.")

        self._capacity = capacity_value

    @property
    def size(self) -> int:
        """Get the size of the jar."""
        return self._size

    @size.setter
    def size(self, size_value: int) -> None:
        if not (isinstance(size_value, int) or 0 < size_value < self._capacity):
            raise ValueError("Size must be non-negative integer smaller than capacity.")

        self._size = size_value


if __name__ == "__main__":
    main()
