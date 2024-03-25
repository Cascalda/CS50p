"""Meal Time."""


def main() -> None:
    """Interface to control all other functions"""

    user_input = input("What time is it? ")
    hours = convert(user_input)

    results = meal_time_teller(int(hours))
    print(results)


def convert(time: str) -> float:
    "Converts time to hours."

    hour_minute_pair, *suffix = time.split(" ")
    hour, minute = hour_minute_pair.split(":")
    hour, minute = int(hour), int(minute)

    if "p.m." in suffix:
        hour += 12

    time_to_hour = hour + (minute / 60)
    return time_to_hour


def meal_time_teller(hour: int) -> str | None:
    """Tells you what meal you should be eating at the given time."""

    meal_to_eat = {
        (7 <= hour <= 8): "breakfast time",
        (12 <= hour <= 13): "lunch time",
        (18 <= hour <= 19): "dinner time",
    }

    return meal_to_eat.get(True)


if __name__ == "__main__":
    main()
