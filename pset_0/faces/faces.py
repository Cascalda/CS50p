"""Converting Emoticons to Emojis."""


def main():
    """Interface to control all other functions."""
    user_input = input("Say something with emoticons! ")
    result = convert(user_input)
    print(result)


def convert(message: str) -> str:
    """Convert emojicons in a message to emojis."""
    emojicon_to_emojis = {
        ":)": "🙂",
        ":(": "🙁",
    }

    for emojicon, emoji in emojicon_to_emojis.items():
        message = message.replace(emojicon, emoji)

    return message


if __name__ == "__main__":
    main()
