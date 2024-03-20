"""Password/Username Generator"""

from password_generation import access_key_generators


def main():
    """Interface to control all other functions."""
    while True:
        generator = get_generator_type()
        product = generator()
        print(f"\n{product}")

        if input("\nGenerate another? (y/n) ").lower() != "y":
            break


def get_generator_type():
    """Matches the generator of choice."""
    while True:
        # Prompt "password" instead of "access key" as "password" is more colloquial
        choice = input("\nPassword (P) or Username (U): ").lower()
        match = {
            "p": access_key_generators,
            "u": generate_username,
        }

        generator = match.get(choice, None)

        if generator is None:
            print("Only 'p' or 'u' are accepted.")
        else:
            return generator


def generate_username():
    """Generates a unique username."""
    print("User")


if __name__ == "__main__":
    main()
