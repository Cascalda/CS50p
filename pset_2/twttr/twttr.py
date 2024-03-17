"""Removes vowels in words"""


def main():
    """Interface to control all other functions"""

    user_input = input("Input: ")
    result = vowel_remove(user_input)
    print(result)


def vowel_remove(characters: str) -> str:
    """Removes vowels like twttr does"""
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    shortened = ""
    for char in characters:
        if char not in vowels:
            shortened += char

    return shortened


if __name__ == "__main__":
    main()
