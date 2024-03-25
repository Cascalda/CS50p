"""Converts code into emojis."""
import emoji


def emojizer() -> None:
    """Takes in a string to output it back with emojis."""
    code = input("Input: ")
    emojized = emoji.emojize(code, language="alias")
    print(emojized)


if __name__ == "__main__":
    emojizer()
