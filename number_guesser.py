#!/usr/bin/env python3

import os
import user_prompts
import game

max_tries: int = 7
upper_limit: int = 100

def main():
    user_prompts.welcome_message(max_tries)
    os.system("clear")
    
    playing = True
    while playing:
        user_prompts.display_intro(upper_limit)
        playing = game.play(upper_limit)

if __name__ == "__main__":
    main()