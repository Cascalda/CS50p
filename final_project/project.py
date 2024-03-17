"""Password/Username Generator"""

from password_generation import generate_password

def main():
    """Interface to control all other functions."""
    while True:
        generator = get_generator()
        product = generator()
        print(f"\n{product}")

        if input("\nGenerate another? (y/n) ").lower() != "y":
            break


def get_generator():
    """Matches the generator of choice."""
    while True:
        choice = input("\nPassword (P) or Username (U): ").lower()
        match = {
            "p": generate_password,
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
