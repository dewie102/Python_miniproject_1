#!/usr/bin/env python3

import os
import user_prompts
import game

def main():
    user_prompts.welcome_message()
    os.system("clear")
    
    playing: bool = True
    while playing: # keep playing the game until the user doesn't want to or we crash...
        max_tries: int = 10
        upper_limit: int = 100

        # Ask the user for an upper limit or take the default
        upper_limit = user_prompts.ask_for_upper_limit(upper_limit)
        os.system("clear")

        # Calculate new max tries to be closer to what would be needed to guess
        max_tries = game.get_new_max_tries(upper_limit)

        # Prompt the user to explain the game details and start the game
        user_prompts.display_intro(upper_limit, max_tries)
        os.system("clear")
        game.play(upper_limit, max_tries)

        # Ask the user if they want to play again
        answer: str = user_prompts.ask_to_play_again()
        playing = True if answer == "YES" else False
        os.system("clear")
    
    print("Thank you for playing!")

if __name__ == "__main__":
    main()