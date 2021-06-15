from os import system, chdir
from glob import glob

files = [
    "./forex/main.py",
    "./hangman-game/main.py",
    "./hangman-game/text.py",
    "./junk-file-organizer/text.py",
    "./junk-file-organizer/main.py",
    "./random-password-generator/main.py",
    "./random-password-generator/text.py",
    "./story-generator/text.py",
    "./story-generator/main.py",
]


def check_format():
    for i in files:
        system(f"pycodestyle --show-source --show-pep8 --format=default {i}")


if __name__ == "__main__":
    check_format()
    print("All done!")
