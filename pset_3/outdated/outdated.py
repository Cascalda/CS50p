"""Changes middle endian dates to big endian dates"""

accepted_months = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12",
}


def main():
    """Interface to control all other functions"""

    while True:
        date_user = input("Date: ").strip()

        try:
            result = date_middle_endian_to_big_endian(date_user)
            print(result)
            break

        except (ValueError, RuntimeError) as e:
            print(e)


def date_middle_endian_to_big_endian(date: str) -> str:
    """Formats American dates to ISO dates"""
    # Extracting day, month, year while checking for format validity
    if "/" in date:
        month, day, year = date.split("/")

    elif "," in date:
        month_day, year = date.split(",")
        month, day = month_day.split()
        month = accepted_months.get(month, RuntimeError("Invalid month"))

    else:
        raise RuntimeError("Invalid Delimiters")

    # Checking for date validity
    if int(day) >= 31 or int(month) > 12:
        raise RuntimeError("Invalid date")

    # Date formatting
    return f"{year}-{int(month):02d}-{int(day):02d}"


if __name__ == "__main__":
    main()
