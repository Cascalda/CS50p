"""Gives fuel gauge fractions in percents"""


def main() -> None:
    """Interface to control all other functions"""
    prompt = input("Fraction: ")
    percentage = convert(prompt)
    indication = gauge(percentage)
    print(indication)


def convert(fraction: str) -> int:
    """Converts fuel gauge to percentages"""
    try:
        numerator, denominator = (int(num) for num in fraction.split("/"))

        if denominator == 0:
            raise ZeroDivisionError("Division by 0 is left undefined")
        if numerator > denominator:
            raise ValueError("Only proper fractions are accepted")

        percentage = round((numerator / denominator) * 100)
        return percentage

    except (ValueError, ZeroDivisionError) as e:
        print(e)
        raise


def gauge(percentage: int) -> str:
    """Determines the gauge reading"""

    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
