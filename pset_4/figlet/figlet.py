"""Use pyfiglet to make fonts"""
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()


def main():
    """Interface to control all other functions"""
    try:
        font_converter()
        text = input("Input: ")
        print(figlet.renderText(text))
    except RuntimeError:
        sys.exit("Only empty prompt or prompt with -f or --font is accepted")


def font_converter():
    """Converts text into different fonts"""
    font_command = sys.argv[1:]

    if len(font_command) == 0:
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)

    else:
        prompt, type_ = font_command

        if (
            (len(font_command) == 2)
            and (prompt in ("-f", "--font"))
            and (type_ in figlet.getFonts())
        ):
            figlet.setFont(font=type_)

        else:
            raise RuntimeError


if __name__ == "__main__":
    main()
