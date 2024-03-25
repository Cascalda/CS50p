"""Make a cleaner version of the files containing first and last names."""

from sys import argv, exit as sys_exit
from PIL import Image, ImageOps


def main() -> None:
    """Interface to control all other functions."""
    format_check()

    try:
        _, input_file, output_file = argv[:3]
    except FileNotFoundError:
        sys_exit("File does not exist")

    put_shirt_on(input_file, output_file)


def format_check() -> None:
    """Check the format of command line."""
    length_check()
    file_format_check()


def length_check() -> None:
    """Check for invalid length of command line arguments."""
    desired_arg_num = 3
    if len(argv) < desired_arg_num:
        sys_exit("Too few command-line arguments")

    if len(argv) > desired_arg_num:
        sys_exit("Too many command-line arguments")


def file_format_check() -> None:
    """Check for invalid file formats."""
    files_to_open = argv[1:]
    given_file_types = {file.rsplit(".", maxsplit=1)[-1] for file in files_to_open}
    desired_file_types = {"jpg", "jpeg", "png"}

    if given_file_types > desired_file_types:
        sys_exit("Not a valid file")

    if len(given_file_types) > 1:
        sys_exit("Input and output have different extensions")


def put_shirt_on(file_in: str, file_out: str) -> None:
    """Make the format of a csv file prettier."""
    with (
        Image.open("shirt.png") as overlay,
        Image.open(file_in) as background,
    ):
        in_edit = ImageOps.fit(background, overlay.size)
        in_edit.paste(overlay, mask=overlay)
        in_edit.save(file_out)


if __name__ == "__main__":
    main()
