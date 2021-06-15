from random import choice
import array
from text import DIGITS, LOCASE_CHARACTERS, SYMBOLS, UPCASE_CHARACTERS

BASE_PASSWORD = "zero"
MAX_LENGTH = 12

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS


def create_password(password):
    for _ in range(0, MAX_LENGTH):
        password += choice(COMBINED_LIST)
    return password


if __name__ == "__main__":
    print(create_password(BASE_PASSWORD))
