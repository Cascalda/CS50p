"""Contains the functions that are required for password generation."""

import random
import string
from inspect import stack
from english_words import get_english_words_set

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
WORDS = sorted(get_english_words_set(["web2"], lower=True))


def main() -> None:
    """Interface to control all other functions."""
    while True:
        access_key = access_key_generators()
        print(access_key)

        if input("\nGenerate another? (y/n) ").lower() != "y":
            break


def access_key_generators() -> str:
    """Chooses the type of acess key the user wants."""
    while True:
        # Prompt "password" instead of "access key" as "password" is more colloquial
        choice = input("\nPassword or Passphrase: ").lower()
        match = {
            "password": generate_password,
            "passphrase": generate_passphrase,
        }
        generator = match.get(choice, None)

        if generator is None:
            print("Only 'password' or 'passphrase' are accepted.")
        else:
            access_key = generator()
            return access_key


def generate_passphrase() -> str:
    """Generates a secure passphrase."""
    length = get_valid_length(MIN_PASSPHRASE_WORDS, MAX_PASSPHRASE_WORDS)
    separator = get_separator()

    # Used random.sample to avoid repeating words,
    # making it harder to be brute-forced, especially for short passphrases
    return f"{separator}".join(random.sample(WORDS, k=length))


def generate_password() -> str:
    """Generates a secure password."""
    length = get_valid_length(MIN_PASSWORD_CHARACTERS, MAX_PASSWORD_CHARACTERS)
    included_flags = get_flags()

    character_pool = "".join(CHARACTERS[flag] for flag in included_flags)

    # Used random.choices to allow repetition, which increases unpredictability
    return "".join(random.choices(character_pool, k=length))


def get_valid_length(min_length: int, max_length: int) -> int:
    """Obtain a valid length from the user."""
    print(
        f"""
          Length must be between {min_length} and {max_length}.
        """
    )

    morpheme_type = {
        "generate_password": "character",
        "generate_passphrase": "word",
    }
    caller = stack()[1].function

    while True:
        morpheme = morpheme_type.get(caller, None)

        try:
            length = int(input(f"\nEnter length of {morpheme}: "))
        except ValueError:
            print("\nOnly integers are accepted.")
            continue

        if min_length <= length <= max_length:
            return length

        print("\nInvalid length. Please try again.")


def get_flags() -> set[str]:
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
            include_flag = input(f"\nInclude {flag}? ").lower() == "y"
            if include_flag:
                flags_included.add(flag)

    return flags_included


def get_separator(max_length: int = 2, default: str = "_") -> str:
    """Obtains a valid separator from the user."""

    while True:
        separator = input(f"Enter separator (Defaulted to {default}): ") or default
        if len(separator) <= max_length:
            return separator

        print(f"Up to {max_length} characters are accepted.")


if __name__ == "__main__":
    main()
