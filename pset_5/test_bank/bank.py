"""Gives the appropriate money for appropriate greeting"""


def main():
    """Interface to control all other functions"""
    user_input = input("Greeting: ")
    results = value(user_input)
    print(f"${results}")


def value(greeting):
    """Money for greeting"""
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
