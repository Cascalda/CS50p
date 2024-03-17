"""Prints out the pretty menu of regular and sicilian pizzas."""
from sys import argv, exit
from tabulate import tabulate
from csv import DictReader


def main():
    """Interface to control all other functions."""
    format_check()

    try:
        file = argv[1]
    except FileNotFoundError:
        exit("File does not exist")

    pretty_menu = prettify_menu(file)
    return pretty_menu


def format_check():
    """Check the format of command line."""
    desired_arg_num = 2

    if len(argv) < desired_arg_num:
        exit("Too few command-line arguments")
    elif len(argv) > desired_arg_num:
        exit("Too many command-line arguments")

    file_to_open = argv[1]
    desired_file_type = "csv"

    if not file_to_open.endswith(f".{desired_file_type}"):
        exit(f"Not a csv file. Perhaps missing '.{desired_file_type}'?")


def prettify_menu(file):
    """Make the format of a csv file prettier."""
    with open(file, mode="r") as csvfile:
        menu = DictReader(csvfile)
        pretty_menu = tabulate(menu, headers="keys", tablefmt="grid")

    return pretty_menu


if __name__ == "__main__":
    result = main()
    print(result)
