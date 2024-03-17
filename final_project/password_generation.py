"""Contains the functions that are required for password generation."""

import random
import string

MINIMUM_LENGTH = 8
MAXIMUM_LENGTH = 128
FLAG_TO_CHARACTERS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "numbers": string.digits,
    "special characters": string.punctuation,
}


def main() -> None:
    """Interface to control all other functions."""
    password = generate_password()
    print(password)


def generate_password() -> str:
    """Generates a secure password."""
    length = get_valid_length()
    included_flags = get_flags()

    character_pool = "".join(FLAG_TO_CHARACTERS[flag] for flag in included_flags)

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password


def get_valid_length() -> int:
    """Obtain a valid password length from the user."""
    while True:
        print(
            """
              Password length should be between 8 and 128 characters long.
              """
        )

        try:
            length = int(input("Enter password length: "))
        except ValueError:
            print("Only integers are accepted.")
            continue

        if MINIMUM_LENGTH <= length <= MAXIMUM_LENGTH:
            return length


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
        for flag in FLAG_TO_CHARACTERS:
            prompt = f"Include {flag}? "
            include_flag = input(prompt).lower() == "y"
            if include_flag:
                flags_included.add(flag)

    return flags_included

    # --------------------------------------------
    flags = {key: False for key in FLAG_TO_CHARACTERS}

    while not any(flags.values()):
        print(
            """
            Press y if u wish to include the following, skipping otherwise:
            - At least 1 condition is required.
            """
        )
        for flag_type in flags:
            prompt = f"Include {flag_type}? "
            flags[flag_type] = input(prompt).lower() == "y"

    return flags


if __name__ == "__main__":
    main()
