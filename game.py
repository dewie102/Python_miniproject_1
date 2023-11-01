import user_prompts

def calculate_next_guess(low, high):
    middle = low + ((high - low) / 2)
    return middle


def process_high_or_low_response(response, low, high, guess):
    if(response == "HIGH"):
        high = guess - 1
    else:
        low = guess + 1

    return {"low": low, "high": high}


def play(upper_limit):
    low = 0
    high = upper_limit

    for count in range(max_tries):
        guess = calculate_next_guess(low, high)
        correct_guess = user_prompts.display_guess(guess)

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