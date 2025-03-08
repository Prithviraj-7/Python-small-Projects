
"""                                                   GAME OF ROCK,PAPER AND SCISSORS                                           """


import random

# Rule: Enter your choice in uppercase: 'R' for Rock, 'P' for Paper, 'S' for Scissors

youdict = {"R": 1, "P": -1, "S": 0}
reversedict = {1: "Rock", -1: "Paper", 0: "Scissors"}

your_score = 0
computer_score = 0

while True:
    computer = random.choice([1, -1, 0])
    youstr = input("Enter your choice (R, P, S) or 'Q' to quit: ")
    
    if youstr.upper() == 'Q':
        print(f"Final Scores - You: {your_score}, Computer: {computer_score}")
        print("Thanks for playing! Goodbye.")
        break
    
    if youstr not in youdict:
        print("Invalid input! Please enter 'R', 'P', or 'S'.")
        continue
    
    you = youdict[youstr]
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")

    if computer == you:
        print("It's a DRAW")
    elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
        print("You Win!")
        your_score += 1
    else:
        print("You Lose!")
        computer_score += 1
    
    print(f"Current Scores - You: {your_score}, Computer: {computer_score}")
    print("\n-------------------\n")

