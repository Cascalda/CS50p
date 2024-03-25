"""Gives the appropriate money for appropriate greeting."""


def main() -> None:
    """Interface to control all other functions."""
    user_input = input("Greeting: ")
    cleansed_greeting = user_input.strip().lower()

    results = financial_reward(cleansed_greeting)
    print(f"${results}")


def financial_reward(greeting: str) -> int:
    """Money for greeting."""
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20

    return 100


if __name__ == "__main__":
    main()
