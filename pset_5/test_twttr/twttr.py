"""Removes vowels in words"""


def main():
    """Interface to control all other functions"""

    user_input = input("Input: ")
    result = shorten(user_input)
    print(result)


def shorten(characters):
    """Removes vowels like twttr does"""
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    shortened = ""
    for char in characters:
        if char not in vowels:
            shortened += char

    return shortened


if __name__ == "__main__":
    main()
