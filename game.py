import user_prompts
import random

def calculate_next_guess(low, high, first_guess):
    guess: int = 0
    if(first_guess):
        guess = random.randint(low, high)
    else:
        guess = (int)(low + ((high - low) / 2))
    
    return guess


def process_high_or_low_response(response, low, high, guess):
    if(response == "HIGH"):
        high = guess - 1
    else:
        low = guess + 1

    return {"low": low, "high": high}


def play(upper_limit, max_tries):
    low = 0
    high = upper_limit
    first_guess = True

    for count in range(max_tries):
        guess = calculate_next_guess(low, high, first_guess)
        correct_guess = user_prompts.display_guess(guess)

        first_guess = False

        if(correct_guess == "YES"):
            print("YES! Told you I could beat you!")
            return True
        else:
            high_or_low = user_prompts.display_high_low_question()
            new_values = process_high_or_low_response(high_or_low, low, high, guess)
            low = new_values["low"]
            high = new_values["high"]

    return False

if __name__ == "__main__":
    calculate_next_guess()