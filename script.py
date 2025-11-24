import random 

while True:
    print("---Welcome to Rock Paper Scissors---")

    user_score=0
    comp_score=0
    ties=0

    name=input('Enter your name: ')
    print("""
    Winning Rules:
    1. Paper vs Rock --> Paper
    2. Rock vs Scissors --> Rock
    3. Scissors vs Paper --> Scissors""")
    print()

    print("""Choices are:
    1. Rock
    2. Paper
    3. Scissors
        """)
    choice=int(input("Enter your choice from 1-3:"))
    print()
    
    while choice > 3 or choice <1:
        choice=int(input("Enter valid input: "))

    if choice == 1:
        user_choice="Rock"

    elif choice == 2:
        user_choice="Paper"

    else:
        user_choice="Scissors"

    print("The user's choice is", user_choice)
    print("Now it is Computer's turn")

    computer=random.randint(1,3)

    if computer==1:
        comp_choice="Rock"

    elif computer==2:
        comp_choice="Paper"

    else:
        comp_choice="Scissors"

    print("The computer's choise is", comp_choice)

    if (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper"):
        print("Paper wins.")
        result="Paper"

    elif(user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors"):
        print("Rock wins.")
        result="Rock"

    elif(user_choice == "Paper" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Paper"):
        print("Scissors wins.")
        result="Scissors"

    else:
        print("It's a tie.")
        result="Tie"

    print()

    if result == "Tie":
        ties += 1

    elif result == user_choice:
        print(name, "wins.")
        user_score +=1

    else:
        print("Computer wins.")
        comp_score +=1

    print()

    print("Scores are")
    print(name,"'s score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties are", ties)

    print()



