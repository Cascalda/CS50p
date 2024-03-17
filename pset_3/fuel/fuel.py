"""Gives fuel gauge fractions in percents"""


def main():
    """Interface to control all other functions"""

    while True:
        obtained_fuel_gauge = input("Fraction: ")

        try:
            calculated_percentage = convert(obtained_fuel_gauge)
        except ValueError:
            print("Only fractions are accepted")
        except (ZeroDivisionError, RuntimeError) as e:
            print(e)
        else:
            break

    result = gauge(int(calculated_percentage))
    print(result)


def convert(fraction: str) -> float:
    """Converts fuel gauge to percentages"""

    numerator, denominator = [int(num) for num in fraction.split("/")]
    if denominator == 0:
        raise ZeroDivisionError("Division by 0 is undefinable")

    if numerator > denominator:
        raise RuntimeError("Only proper fractions are accepted")

    percent = (numerator / denominator) * 100
    return percent


def gauge(percentage: int) -> str:
    """Determines the gauge reading"""

    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"

    return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
