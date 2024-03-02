from random import choice
from english_text import (
    FIRST_SENTENCE,
    MAIN_CHARACTER,
    TIME,
    PLOT,
    PLACE,
    SECOND_CHARACTER,
    AGE,
    WORK,
)
from french_text import (
    PREMIERE_PHRASE,
    PERSONNAGE_PRINCIPAL,
    TEMPS,
    INTRIGUE,
    DEUXIEME_PERSONNAGE,
    AGE_FRENCH,
    TRAVAIL,
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
HISTOIRE = (
    choice(PREMIERE_PHRASE)
    + choice(PERSONNAGE_PRINCIPAL)
    + choice(TEMPS)
    + choice(INTRIGUE)
    + choice(DEUXIEME_PERSONNAGE)
    + choice(AGE_FRENCH)
    + choice(TRAVAIL)
)

if __name__ == "__main__":
    language = input("Hi! Do you want the story in French or English? Reply with FRENCH or ENGLISH: ")
    if(language == "FRENCH"):
        print(HISTOIRE)
    elif(language == "ENGLISH"):
        print(STORY)
    else:
        print("You didn't put the right input!")
