import random 

ch = ["Stone","Paper","Scissor"]

#Funcations:

def ans():
    global user_answers,cp_answers
    user_answers = input(f"chose one of the following items {ch}.").lower()
    cp_answers = random.choice(ch).lower()

cp_score = 0
us_score = 0
def winner():
    global user_answers,cp_answers,us_score,cp_score

    if ((user_answers == "stone" and cp_answers == "scissor") or 
        (user_answers == "scissor" and cp_answers == "paper") or 
        (user_answers == "paper" and cp_answers == "stone")):
        us_score = us_score + 1
        print("User wins this game.")

    elif ((cp_answers == "stone" and user_answers == "scissor") or 
          (cp_answers == "scissor" and user_answers == "paper") or 
          (cp_answers == "paper" and user_answers == "stone")):
        cp_score = cp_score + 1
        print("Computer wins this game")

    else:
        print("It is a tie")

def results():
    global us_score,cp_score
    print(f"The user score is {us_score}")
    print(f"The computer score is {cp_score}")
    if us_score > cp_score:
        print("User wins this match")
    else:
        print("Computer wints this match")


def main():
    while True:
        user_choice = input("Do you want to play this game?  (Yes/No)").lower()
        if user_choice == "yes":
            ans()
            winner()
        else:
            results()
            break


#starting
main()