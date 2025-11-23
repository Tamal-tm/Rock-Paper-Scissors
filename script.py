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
