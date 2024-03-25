"""Make a cleaner version of the files containing first and last names."""

from sys import argv, exit as sys_exit
from csv import DictReader, DictWriter


def main() -> None:
    """Interface to control all other functions."""
    format_check()

    try:
        _, input_file, output_file = argv[:3]
    except FileNotFoundError:
        sys_exit("File does not exist")

    scourgify(input_file, output_file)


def format_check() -> None:
    """Check the format of command line."""
    desired_arg_num = 3

    if len(argv) < desired_arg_num:
        sys_exit("Too few command-line arguments")
    elif len(argv) > desired_arg_num:
        sys_exit("Too many command-line arguments")

    files_to_open = argv[1:]
    desired_file_type = "csv"

    for file in files_to_open:
        if not file.endswith(f".{desired_file_type}"):
            sys_exit(f"Not a csv file. Perhaps missing '.{desired_file_type}'?")


def scourgify(file_in: str, file_out: str) -> None:
    """Make the format of a csv file prettier."""
    with (
        open(file_in, mode="r", encoding="utf-8") as csv_in,
        open(file_out, mode="w", encoding="utf-8") as csv_out,
    ):
        csv_in = DictReader(csv_in)
        fieldnames = ("first", "last", "house")
        csv_out = DictWriter(csv_out, fieldnames=fieldnames)

        csv_out.writeheader()
        for row in csv_in:
            last_name, first_name = row["name"].split(", ")
            house = row["house"]
            csv_out.writerow(
                {
                    "first": first_name,
                    "last": last_name,
                    "house": house,
                }
            )


if __name__ == "__main__":
    main()
