"""Gives the appropriate money for appropriate greeting."""


def main() -> None:
    """Interface to control all other functions."""
    user_input = input("Greeting: ")
    results = value(user_input)
    print(f"${results}")


def value(greeting: str) -> int:
    """Money for greeting."""
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
