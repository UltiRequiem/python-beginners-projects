import os
from pathlib import Path

from text import DIRECTORIES


FILE_FORMATS = {
    file_format: directory
    for directory, file_formats in DIRECTORIES.items()
    for file_format in file_formats
}


def main():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

    try:
        os.mkdir("OTHER-FILES")
    except BaseException:
        pass

    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(
                    os.getcwd() + "/" + str(Path(dir)),
                    os.getcwd() + "/OTHER-FILES/" + str(Path(dir)),
                )

        except Exception as exception:
            print(f"Oops!, {exception} ocurred.")


if __name__ == "__main__":
    main()
