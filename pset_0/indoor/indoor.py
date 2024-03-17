"""Makes loud apparent internet speech into soft speech."""


def main():
    """Interface to control all other functions."""
    indoor_voice()


def indoor_voice():
    """Reduce the apparent volume of an outdoor voice."""
    outdoor_voice = input("Scream!!!")
    print(outdoor_voice.lower())


if __name__ == "__main__":
    main()
