import user_prompts
import random
import os
import math

# On the first guess we will give a random guess to keep it interesting
def calculate_next_guess(low, high, first_guess) -> int:
    guess: int = 0
    if(first_guess):
        guess = random.randint(low, high)
    else:
        # Take the midpoint and ask that
        guess = (int)(low + ((high - low) / 2))
    
    return guess


def process_high_or_low_response(response, low, high, guess) -> dict[str, int]:
    # Figure out if we need to change the high or low bound before amking a new guess
    if(response == "HIGH"):
        high = guess - 1
    else:
        low = guess + 1

    # return a dictionary for easy reassignment
    return {"low": low, "high": high}


def get_new_max_tries(upper_limit) -> int:
    # Take the log of the upper limit, this gives the number of tries needed to get it correct
    tries = (int)(math.log(upper_limit, 2))

    # add in a random number 2 above and below this amount to ensure the player can win
    tries += random.randint(-1, 1)

    return tries


def play(upper_limit, max_tries) -> None:
    low = 0
    high = upper_limit
    first_guess = True

    for count in range(max_tries):
        # Get our guess
        guess = calculate_next_guess(low, high, first_guess)
        print(f"ROUND: {count + 1}")
        # Ask the player if it is correct
        correct_guess = user_prompts.display_guess(guess)

        first_guess = False

        if(correct_guess == "YES"):
            # We win, give details of the game and return
            os.system("clear")
            if(guess == 69 or guess == 420):
                print("HAHA... nice")

            print("YES! Told you I could beat you!")
            print(f"You lasted {count + 1} rounds, good job!")
            return
        else:
            # We didn't get it, ask the user if we were high or low
            high_or_low = user_prompts.display_high_low_question()
            os.system("clear")
            # Get the new upper or lower bounds for the next guess
            new_values = process_high_or_low_response(high_or_low, low, high, guess)
            low = new_values["low"]
            high = new_values["high"]
    
    # We have exceeded the max tries and the user won
    print("I admit defeat, you have won...")
