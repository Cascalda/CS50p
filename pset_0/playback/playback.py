"""Repeats what the user has said but with playful delay."""


def main():
    """Interface to control all other functions."""
    result = play_it_back()
    print(result)


def play_it_back() -> str:
    """Play what the user said back to them with style."""
    message = input("Whatcha say?? ")
    return message.replace(" ", "...")


if __name__ == "__main__":
    main()
