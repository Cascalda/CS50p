"""Provides calories of the given fruit"""


def main():
    """Interface to control all other functions"""

    given_fruit = input("Item: ").lower()

    calories = calories_of_fruit(given_fruit)
    print(calories)


def calories_of_fruit(fruit: str) -> int | str:
    """Provides calories of given fruit"""

    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }
    null_output = ""
    return fruits.get(fruit, null_output)


if __name__ == "__main__":
    main()
