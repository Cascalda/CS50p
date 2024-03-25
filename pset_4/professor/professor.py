"""Implement a simple program that mimics the Little Professor calculator toy."""

from random import randint


def main() -> None:
    """Interface to control all other functions."""
    level = get_level()
    integer_pairs_with_answers = generate_integers(level)

    score = 0
    for (x, y), answer in integer_pairs_with_answers:
        wrong_answers = 0
        while wrong_answers < 3:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == answer:
                score += 1
                break

            wrong_answers += 1
            print("EEE")

        if wrong_answers == 3:
            print(f"\n{x + y}")

    print(f"Score: {score}")


def get_level() -> int:
    """Get the level from the user"""
    levels = (1, 2, 3)
    while True:
        try:
            if (user_input := int(input("Level: "))) in levels:
                return user_input
        except ValueError as e:
            print(f"{e}: Only integers between 1 and 3 are accepted")


# No type annotation for return as it is too complex
def generate_integers(level: int):
    """Generates a specified number of random integer pairs."""
    start = 10 ** (level - 1) if level > 1 else 0
    stop = 10**level
    count = 10

    integer_pairs = ((randint(start, stop), randint(start, stop)) for _ in range(count))
    integer_pairs_with_answers = (((x, y), (x + y)) for (x, y) in integer_pairs)

    return integer_pairs_with_answers


if __name__ == "__main__":
    main()
