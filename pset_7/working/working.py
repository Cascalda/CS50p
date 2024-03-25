"""Converts time from 12-hour format to 24-hour format."""

import re

TIME_SEPARATOR = "to"
TIME_MATCH = r"""([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"""
TIME_INPUT_MATCH = f"{TIME_MATCH} {TIME_SEPARATOR} {TIME_MATCH}"


def main() -> str:
    """Interface to control all other functions."""
    time_12_hour = input("Hours: ")
    result = convert(time_12_hour)
    return result


def convert(time: str) -> str:
    """Converts 12-hour time to 24-hour time."""
    if match := re.fullmatch(TIME_INPUT_MATCH, time):
        time_from = format_24_hour(
            match.group(3), int(match.group(1)), int(match.group(2))
        )
        time_to = format_24_hour(
            match.group(6), int(match.group(4)), int(match.group(5))
        )
        result = f"{time_from} {TIME_SEPARATOR} {time_to}"
        return result

    raise ValueError


def format_24_hour(meridiem: str, hour: int, minute: int = 0) -> str:
    """Formats time to 24-hour from 12-hour."""
    # hour = int(hour)
    # minute = int(minute) if minute else 0

    if meridiem == "PM" and hour != 12:
        hour = (hour + 12) % 24
    elif meridiem == "AM" and hour == 12:
        hour = 0

    result = f"{hour:02d}:{minute:02d}"
    return result


if __name__ == "__main__":
    RESULT = main()
    print(RESULT)
