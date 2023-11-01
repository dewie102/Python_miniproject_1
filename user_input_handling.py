def get_yes_or_no(prompt) -> str:
    response = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").strip().lower()

        check_for_quit(answer)

        if(answer == "y"):
            response = "YES"
            valid_answer = True
        elif(answer == "n"):
            response = "NO"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response


def get_high_or_low(prompt) -> str:
    response = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").strip()

        check_for_quit(answer.lower())

        if(answer == "1"):
            response = "HIGH"
            valid_answer = True
        elif(answer == "2"):
            response = "LOW"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response


def get_number(prompt, default_max) -> int:
    response = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt + f" [{default_max}]")
        answer = input("> ").strip()

        check_for_quit(answer.lower())

        if(answer == ""):
            valid_answer = True
            response = default_max

        if(answer.isdigit()):
            try:
                number = int(answer)
                if(number >= 10000000):
                    print("Come on... do you even know numbers that high?")
                    print("Try again")
                else:
                    response = number
                    valid_answer = True
            except Exception as e:
                print(f"Error, something happend:\n{e}")
        else:
            print("Invalid response, please try again")

    return response


def check_for_quit(input) -> None:
    if(input == "q" or input == "quit"):
        print("Quitting.... Thanks for playing!")
        quit()
