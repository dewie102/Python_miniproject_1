def get_yes_or_no(prompt):
    response = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").strip().lower()

        if(answer == "y"):
            response = "YES"
            valid_answer = True
        elif(answer == "n"):
            response = "NO"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response


def get_high_or_low(prompt):
    response = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").strip()

        if(answer == "1"):
            response = "HIGH"
            valid_answer = True
        elif(answer == "2"):
            response = "LOW"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response