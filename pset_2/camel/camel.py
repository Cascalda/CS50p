"""Convert camelCase characters into snake case"""


def main():
    """Interface to control all other functions"""

    user_input = input("camelCase: ")

    result = snake_caser(user_input)
    print(result)


def snake_caser(camel_case: str) -> str:
    """Brings the snake_case out of camelCase"""

    snake_cased = ""

    for char in camel_case:
        if char.islower():
            snake_cased += char
        else:
            to_snake_case = f"_{char.lower()}"
            snake_cased += to_snake_case

    return snake_cased


if __name__ == "__main__":
    main()
