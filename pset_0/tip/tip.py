"""Finds the appropriate tip given the cost and rate."""


def main():
    """Interface to control all other functions."""
    dollars = get_dollars(input("How much was the meal? "))
    percent = get_percentage(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def get_dollars(meal_price: str) -> float:
    """Return the conversion of dollar to float."""
    return float(meal_price[1:])


def get_percentage(tip_ratio: str) -> float:
    """Return the conversion of rate percent to float."""
    percent_value = int(tip_ratio[:-1])
    return percent_value / 100


if __name__ == "__main__":
    main()
