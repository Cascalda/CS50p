"""Convert ISO 8601 formattd dates to words."""

from datetime import date
import sys
import inflect


inflect = inflect.engine()
number_to_words = inflect.number_to_words


def main() -> None:
    """Interface to control all other functions."""
    date_of_birth_input = input("Date of Birth: ")
    date_of_birth = validify_date_of_birth(date_of_birth_input)

    age_minutes = calculate_age_in_minutes(date_of_birth)
    result = convert_age_to_words(age_minutes)
    print(result)


def validify_date_of_birth(date_of_birth_input: str) -> date:
    """Validifies the date of birth provided."""
    try:
        date_of_birth = date.fromisoformat(date_of_birth_input)
        return date_of_birth
    except ValueError:
        sys.exit("Invalid date")


def calculate_age_in_minutes(date_of_birth: date) -> int:
    """Calculates age in minutes according to todays date."""
    today_date = date.today()
    age = today_date - date_of_birth
    age_minutes = int(age.total_seconds() // 60)

    return age_minutes


def convert_age_to_words(age_minutes: int) -> str:
    """Converts age in numbers to words."""
    display_age_minutes = number_to_words(age_minutes, andword="").capitalize()
    result = f"{display_age_minutes} minutes"

    return result


if __name__ == "__main__":
    main()
