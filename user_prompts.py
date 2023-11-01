import pyfiglet
from user_input_handling import get_yes_or_no, get_high_or_low

def welcome_message(max_tries):
    print(pyfiglet.figlet_format("Welcome to Number Guesser!"))
    print()
    print(f"The game were I guess the number you are thinking in {max_tries} tries or less")
    input("press enter to continue...")


def display_intro(upper_range):
    print(f"Think of a number between 0 and {upper_range}")
    input("Press enter when ready to continue")


def display_guess(guess):
    return get_yes_or_no(f"Is your number: {guess}? [y/n]")


def display_high_low_question():
    return get_high_or_low(f"Was the guess too high or too low?\n1. Too High\n2. Too Low")

if __name__ == "__main__":
    welcome_message()