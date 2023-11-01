import pyfiglet

def welcome_message(max_tries):
    print(pyfiglet.figlet_format("Welcome to Number Guesser!"))
    print()
    print(f"The game were I guess the number you are thinking in {max_tries} tries or less")
    input("press enter to continue...")


def display_intro(upper_range):
    print(f"Think of a number between 0 and {upper_range}")
    input("Press enter when ready to continue")


if __name__ == "__main__":
    welcome_message()