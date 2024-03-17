"""Records and displays the users groceries list"""


def grocery_maker() -> None:
    """Makes groceries and displays them"""
    groceries_list = {}

    while True:
        try:
            item = input().upper()

            if item not in groceries_list:
                groceries_list.update({item: 1})
            else:
                groceries_list[item] += 1

        except EOFError:
            for item, amount in sorted(groceries_list.items()):
                print(f"{amount} {item}")
            break


if __name__ == "__main__":
    grocery_maker()
