import random

from text import ABC, HANGMAN, WORDS


def get_random_word() -> str:
    return random.choice(WORDS)


def restart() -> None:
    global missed_letters, correct_letters, game_is_done, secret_word
    missed_letters = ""
    correct_letters = ""
    game_is_done = False
    secret_word = get_random_word()


def display_board(HANGMAN, missed_letters, correct_letters, secret_word) -> None:
    print(HANGMAN[len(missed_letters)] + "\n")

    print("Missed Letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print("\n")

    blanks = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1 :]

    for letter in blanks:
        print(letter, end=" ")
    print("\n")


def get_guess(already_guessed) -> str:
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in ABC:
            print("Please enter a normal letter.")
        else:
            return guess


def play_again() -> bool:
    return input("\nDo you want to play again? ").lower().startswith("y")


if __name__ == "__main__":

    missed_letters = ""
    correct_letters = ""
    secret_word = get_random_word()
    game_is_done = False

    while True:
        display_board(HANGMAN, missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('\nYes! The secret word is "' + secret_word + '"! You have won!')
                game_is_done = True
        else:
            missed_letters = missed_letters + guess

            if len(missed_letters) == len(HANGMAN) - 1:
                display_board(HANGMAN, missed_letters, correct_letters, secret_word)
                print(
                    "You have run out of guesses!\nAfter "
                    + str(len(missed_letters))
                    + " missed guesses and "
                    + str(len(correct_letters))
                    + ' correct guesses, the word was "'
                    + secret_word
                    + '"'
                )
                game_is_done = True

        if game_is_done:
            if play_again():
                restart()
            else:
                break
