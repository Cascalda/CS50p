"""Vanity Plates and whether they are valid"""
from string import punctuation


def main():
    """Interface to control all other functions"""

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_char):
    """Checks validity of vanity plates"""

    validity_checks = {
        "First 2 Characters": plate_char[0:2].isalpha(),
        "Length": 2 <= len(plate_char) <= 6,
        "Special Characters": not (
            set(plate_char) & set(punctuation)
        ),  # Vanity plates don't contain special characters
        "Number Conditions": num_condition_check(plate_char),
    }

    return all(validity_checks.values())


def num_condition_check(plate_to_check):
    """To validate conditions for numbers in the plate"""

    for index, char in enumerate(plate_to_check):
        if char.isdigit():
            if int(char) == 0:  # first digit is 0
                return False

            return plate_to_check[
                index:
            ].isdigit()  # all succeeding characters are digits

    return True  # no digits


if __name__ == "__main__":
    main()
