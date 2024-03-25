"""Calculates the number of lines in a file."""

from sys import argv, exit as sys_exit


def main() -> int:
    """Interface to control all other functions."""
    format_check()

    try:
        file = argv[1]
    except FileNotFoundError:
        sys_exit("File does not exist")

    num_lines = get_lines(file)
    return num_lines


def format_check() -> None:
    """Check the format of command line."""
    desired_arg_num = 2

    if len(argv) < desired_arg_num:
        sys_exit("Too few command-line arguments")
    elif len(argv) > desired_arg_num:
        sys_exit("Too many command-line arguments")

    file_to_open = argv[1]
    desired_file_type = "py"

    if not file_to_open.endswith(f".{desired_file_type}"):
        sys_exit(f"Not a csv file. Perhaps missing '.{desired_file_type}'?")


def get_lines(file: str) -> int:
    """Get the number of lines in a file."""

    def is_empty_line(line):
        empty_line_condition = (not line, line.startswith("#"))
        return any(empty_line_condition)

    with open(file, mode="r", encoding="utf-8") as pyfile:
        lines = [_.strip(" \n") for _ in pyfile.readlines()]
        lines_total = len(lines)

        for line in lines:
            if is_empty_line(line):
                lines_total -= 1

        return lines_total


if __name__ == "__main__":
    result = main()
    print(result)
