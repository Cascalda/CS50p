"""Exchange currency for bitcoin."""

import sys
import requests


def main() -> None:
    """Interface to control all other functions."""
    bitcoins_requested = bitcoins_to_get()
    bitcoins_in_usd = bitcoin_to_usd(bitcoins_requested)
    print(f"${bitcoins_in_usd:,.4f}")


def bitcoins_to_get() -> str:
    """The number of bitcoins the user wants to get."""
    try:
        return sys.argv[1]
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument must be a number")


def bitcoin_to_usd(bitcoins: str) -> float:
    """Provides the rate conversion of bitcoin currently."""
    try:
        data = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5
        ).json()
        rate_float = data["bpi"]["USD"]["rate_float"]
        return float(bitcoins) * rate_float
    except requests.exceptions.JSONDecodeError:
        sys.exit()


if __name__ == "__main__":
    main()
