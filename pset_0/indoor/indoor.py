"""Makes loud apparent internet speech into soft speech."""


def main() -> None:
    """Interface to control all other functions."""
    print(indoor_voice())


def indoor_voice() -> str:
    """Reduce the apparent volume of an outdoor voice."""
    outdoor_voice = input("Scream!!!")
    return outdoor_voice.lower()


if __name__ == "__main__":
    main()
