#!/usr/bin/env python3

import os
import user_prompts

max_tries: int = 7
upper_limit: int = 100

def main():
    user_prompts.welcome_message(max_tries)
    os.system("clear")
    
    playing = True
    while playing:
        user_prompts.display_intro(upper_limit)

        for count in range(max_tries):
            print(count)

        playing = False


if __name__ == "__main__":
    main()