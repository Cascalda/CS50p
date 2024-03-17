"""Provides the due or owed amount according to coins given"""


def main():
    """Interface to control all other functions"""

    result = coke_machine()
    print(result)


def coke_machine() -> str:
    """Tells you amount due until you paid at least 50 cents"""

    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")

        cents_given = int(input("Insert Coin: "))

        accepted = [5, 10, 25]
        if cents_given in accepted:
            amount_due -= cents_given

    change_owed = -amount_due
    return f"Change Owed: {change_owed}"


if __name__ == "__main__":
    main()
