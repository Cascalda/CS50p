"""Checks your answer to the question what is the answer to everything.
    - A reference to Hitchhiker's Guide to the Galaxy
"""

ANSWERS = ("42", "forty-two", "forty two")


def main() -> None:
    """Interface to control all other functions."""
    question = """
    What's the answer to the Great Question of Life,
    the Universe,
    and Everything?
    """
    user_input = input(question)
    deep_answer(user_input.lower().strip())


def deep_answer(answer: str) -> None:
    """Provides a thought provoking answer."""
    if answer in ANSWERS:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
