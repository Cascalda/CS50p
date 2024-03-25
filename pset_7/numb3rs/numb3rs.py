"""Check if IPv4 Addresses are valid."""

import re


def main() -> bool:
    """Interface to control all other functions."""
    ip_address = input("IPv4 Address: ")
    result = validate(ip_address)
    return result


def validate(ip_address: str) -> bool:
    """Validate IPv4 address."""
    octets = ip_address.split(".")
    octet_amount = 4
    if len(octets) != octet_amount:
        return False

    for octet in octets:
        if not re.fullmatch(
            r"""
            25[0-5] # Match 250 - 255
            |2[0-4][0-9] # Match 200 - 249
            |1?[0-9]{1,2} # Match 0 to 199
            """,
            octet,
            re.VERBOSE,
        ):
            return False

    return True


if __name__ == "__main__":
    RESULT = main()
    print(RESULT)
