"""Contains the functions that are required for password generation."""

import random
import string
from nltk.corpus import wordnet

MIN_PASSWORD_CHARACTERS = 8
MAX_PASSWORD_CHARACTERS = 128

MIN_PASSPHRASE_WORDS = 4
MAX_PASSPHRASE_WORDS = 20

CHARACTERS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "numbers": string.digits,
    "special characters": string.punctuation,
}
WORDS = wordnet.words()


def main() -> None:
    """Interface to control all other functions."""
    password = password_generators()
    print(password)


def password_generators() -> str:
    """Chooses the type of password the user wants."""
    while True:
        choice = input("\nPassword or Passphrase: ").lower()
        match = {
            "password": generate_password,
            "passphrase": generate_passphrase,
        }

        generator = match.get(choice, None)

        if generator is None:
            print("Only 'password' or 'passphrase' are accepted.")
        else:
            return generator


def get_valid_length(min_length: int, max_length: int) -> int:
    """Obtain a valid length from the user."""
    print(
        f"""
        Length must be between {min_length} and {max_length}.
        """
    )
    while True:
        try:
            length = int(input("Enter length: "))
        except ValueError:
            print("Only integers are accepted.")
            continue

        if min_length <= length <= max_length:
            return length

        print("Invalid length. Please try again.")


def generate_passphrase() -> str:
    """Generates a secure passphrase."""
    length = get_valid_length(MIN_PASSPHRASE_WORDS, MAX_PASSPHRASE_WORDS)
    separator = get_separator()

    return f"{separator}".join(random.sample(WORDS, k=length))


def generate_password() -> str:
    """Generates a secure password."""
    length = get_valid_length(MIN_PASSWORD_CHARACTERS, MAX_PASSWORD_CHARACTERS)
    included_flags = get_flags()

    character_pool = "".join(CHARACTERS[flag] for flag in included_flags)
    return "".join(random.choices(character_pool, k=length))


def get_flags() -> dict[bool]:
    """Get valid flags from the user."""
    flags_included = set()

    while not flags_included:
        print(
            """
            Press y if u wish to include the following, skipping otherwise:
            - At least 1 condition is required.
            """
        )
        for flag in CHARACTERS:
            prompt = f"Include {flag}? "
            include_flag = input(prompt).lower() == "y"
            if include_flag:
                flags_included.add(flag)

    return flags_included


def get_separator():
    """Obtains a valid separator from the user."""
    separator_length = 1

    while True:
        separator = input("Enter separator: ")
        if len(separator) == separator_length:
            return separator

        print("Only 1 character is accepted.")


if __name__ == "__main__":
    main()
