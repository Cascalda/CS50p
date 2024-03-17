"""Count the number of 'um's that appear in that text."""
import re


def main():
    """Interface to control all other functions."""
    text = input("Text: ")
    result = count(text)
    return result


def count(text):
    """Count the 'um's in a string"""
    regex = r"\bum\b"
    um_list = re.findall(regex, text, flags=re.IGNORECASE)
    um_total = len(um_list)
    return um_total


if __name__ == "__main__":
    main()
