from random import choice
from text import (
    FIRST_SENTENCE,
    MAIN_CHARACTER,
    TIME,
    PLOT,
    PLACE,
    SECOND_CHARACTER,
    AGE,
    WORK,
)

STORY = (
    choice(FIRST_SENTENCE)
    + choice(MAIN_CHARACTER)
    + choice(TIME)
    + choice(PLOT)
    + choice(PLACE)
    + choice(SECOND_CHARACTER)
    + choice(AGE)
    + choice(WORK)
)

if __name__ == "__main__":
    print(STORY)
