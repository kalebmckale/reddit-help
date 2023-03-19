#!/usr/bin/env python3

import random

# Customizable game constants
MIN_VALUE = 0
MAX_VALUE = 9
HIGHER_OPTION = "+"    # character/symbol user enters to choose "higher"
LOWER_OPTION = "-"     # character/symbol user enters to choose "lower"

# Constants and game prompts
CHOICE = {
    HIGHER_OPTION: 1,
    LOWER_OPTION: -1
}
GAME_START = (
    f"I'll pick a number from {MIN_VALUE} to {MAX_VALUE}.\n"
    f"You have to guess if the next number will be higher ({HIGHER_OPTION}) "
    f"or lower ({LOWER_OPTION}).\nIf you fail, even once, the game is over."
)
USER_CHOICE = (
    "Will the next number be\n"
    f"    ({HIGHER_OPTION}) higher\n"
    f"    ({LOWER_OPTION}) lower\n"
    "Leave choice blank to end the game.\n"
    f"choice [{HIGHER_OPTION}/{LOWER_OPTION}]: "
)

def get_play_choice(num_games):
    PLAY = (
        f"Would you like to play{' again' if num_games else ''}?\n"
        "choice [y/n]: "
    )
    while (choice := input(PLAY).lower()) not in "yn":
        print(f"Invalid choice! 'y' or 'n' expected: '{choice}' entered.")
    return choice

def play_game():
    # initialize win counter
    num_wins = 0

    # select initial random number
    prev_value = random.randint(MIN_VALUE, MAX_VALUE)
    print(f"The number is '{prev_value}'.")

    while True:
        # ask user for input and error (and repeat) if "bad" input or return if blank
        while (guess := input(USER_CHOICE)) not in f"{HIGHER_OPTION}{LOWER_OPTION}":
            print(
                f"Invalid choice! '{HIGHER_OPTION}' or '{LOWER_OPTION}' expected: "
                f"'{guess}' entered"
            )

        # user left choice blank and wants to quit
        if not guess:
            return num_wins

        # select next random number
        while (value := random.randint(MIN_VALUE, MAX_VALUE)) == prev_value:
            pass

        # check user's choice for loss
        if CHOICE[guess] * (value - prev_value) < 0:
            print(f"No, that wasn't it. The number was '{value}'.")
            return num_wins

        # user selected the right number
        print(f"That's right! The number is '{value}'.")
        num_wins += 1
        prev_value = value

def main():
    # the game debriefs the player on the rules and asks to initiate the game
    name = input("What's your name?\n").title()
    print(f"Welcome, {name}!\n{GAME_START}")
    num_games = 0
    while (choice := get_play_choice(num_games)) == "y":
        num_games += 1
        num_wins = play_game()
        print(f"\n--- Game {num_games} Results ---")
        print(f"{name} won a total of {num_wins} times.")

    # user chose 'n' at either GAME_START or PLAY_AGAIN
    print(f"We'll see you next time, {name}!")

if __name__ == "__main__":
    main()