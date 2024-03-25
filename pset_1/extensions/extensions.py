"""Provides the desciption of the file extension."""


def main() -> None:
    """Interface to control all other functions."""
    user_input = input("File name: ")
    *_, extension = user_input.strip().split(".")
    cleansed_input = extension.lower()

    results = extension_descriptor(cleansed_input)
    print(results)


def extension_descriptor(file_extension: str) -> str:
    """Provides short description of file type given its extension."""
    match file_extension:
        case "gif" | "png":
            return f"image/{file_extension}"

        case "jpg" | "jpeg":
            return "image/jpeg"

        case "pdf" | "zip":
            return f"application/{file_extension}"

        case "txt":
            return "text/plain"

        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()
