def get_yes_or_no(prompt):
    reponse = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").trim().lower()

        if(answer == "y"):
            reponse = "YES"
            valid_answer = True
        elif(answer == "n"):
            reponse = "NO"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response


def get_high_or_low(prompt):
    reponse = ""
    valid_answer = False
    while(not valid_answer):
        print(prompt)
        answer = input("> ").trim()

        if(answer == "1"):
            reponse = "HIGH"
            valid_answer = True
        elif(anwer == "2"):
            reponse = "LOW"
            valid_answer = True
        else:
            print("Invalid response, please try again")

    return response