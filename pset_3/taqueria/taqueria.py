"""Computes immediate cost given order"""


def main():
    """Interface to control all other functions"""
    total_cost = 0

    while True:
        try:
            order = input("Item: ").title()
            total_cost += order_payment(order)

            print(f"Total: ${total_cost:.2f}")
        except EOFError:
            print(total_cost)
            break


def order_payment(order_obtained):
    """Gets all the total of the order"""
    taqueria_menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    return taqueria_menu.get(order_obtained, 0.0)


if __name__ == "__main__":
    main()
