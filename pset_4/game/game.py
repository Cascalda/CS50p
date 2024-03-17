"""Have the user participate in a number guessing game given a maximum positive number"""

from random import randint


def main():
    """Interface to control all other functions"""
    my_start = 1
    random_num = randint(my_start, get_level())
    guessing(random_num)


def get_level():
    """Gets the maximum of the range"""
    while True:
        if isvalid(level := input("Level: ")):
            return int(level)


def guessing(random_num):
    """Guides the user to guessing the correct number"""
    print("Guesses accept integers only.")
    while True:
        if not isvalid(guess := input("Guess: ")):
            continue

        guess = int(guess)
        if guess == random_num:
            print("Just right!")
            break

        elif guess < random_num:
            print("Too small!")
        else:
            print("Too large!")


def isvalid(user_input):
    """Checks for validity of user input"""
    if not user_input.isnumeric():
        return False
    if int(user_input) <= 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
