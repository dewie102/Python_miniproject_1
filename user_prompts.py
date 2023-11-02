import pyfiglet
from user_input_handling import get_yes_or_no, get_high_or_low, get_number

def welcome_message() -> None:
    print(pyfiglet.figlet_format("Welcome to Number Guesser!"))
    print()
    print(f"The game were I guess the number you are thinking")
    print("The number of rounds is based on the max number you pick")
    input("press enter to continue...")


def display_intro(upper_range, max_tries) -> None:
    print(f"Think of a number between 0 and {upper_range}")
    print(f"I will have {max_tries} rounds to guess the correct number")
    print("At any point if you want to quit please enter 'q' or 'quit'")
    input("Press enter when ready to continue")


def display_guess(guess) -> str:
    return get_yes_or_no(f"Is your number: {guess}? [y/n]")


def display_high_low_question() -> str:
    return get_high_or_low(f"Was the guess too high or too low?\n1. Too High\n2. Too Low")


def ask_to_play_again() -> str:
    return get_yes_or_no(f"Would you like to play again? [y/n]")


def ask_for_upper_limit(default_max) -> int:
    return get_number(f"Pick an max value to pick a number from", default_max)


def nice_prompt(prompt):
    print(pyfiglet.figlet_format(prompt))
