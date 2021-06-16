from os import system

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


def format():
    for i in files:
        system(f"autopep8 --in-place --aggressive {i}")


if __name__ == "__main__":
    format()
    print("All done!")
