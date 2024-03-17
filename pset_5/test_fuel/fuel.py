"""Gives fuel gauge fractions in percents"""


def main():
    """Interface to control all other functions"""
    prompt = input("Fraction: ")
    percentage = convert(prompt)
    indication = gauge(percentage)
    print(indication)


def convert(fraction):
    """Converts fuel gauge to percentages"""
    try:
        numerator, denominator = (int(num) for num in fraction.split("/"))

        if denominator == 0:
            raise ZeroDivisionError("Division by 0 is left undefined")
        elif numerator > denominator:
            raise ValueError("Only proper fractions are accepted")

        percentage = round((numerator / denominator) * 100)
        return percentage

    except (ValueError, ZeroDivisionError) as e:
        print(e)
        raise


def gauge(percentage):
    """Determines the gauge reading"""

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
