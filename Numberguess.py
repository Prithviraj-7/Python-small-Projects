import random


while True:  # This ensures the game restarts after each round
    target = random.randint(1, 100)  # Generate a new target number each round
    print("\n🎯 Welcome to the Number Guessing Game! 🎯")
    print("Guess the number between 1 and 100.")
    print("Enter 'Q' to quit or 'Ans' to reveal the answer.")

    while True:
        Userchoice = input("Guess the Number: ").strip().upper()

        if Userchoice == "Q":
            print("You chose to quit. Goodbye! 👋")
            exit()  

        elif Userchoice == "ANS":
            print(f"The correct number was {target}. \n --'BETTER LUCK NEXT TIME'--")
            break  

        if not Userchoice.isdigit():
            print("❌ Invalid input! Please enter a number.")
            continue  

        Userchoice = int(Userchoice)

        if Userchoice == target:
            print("🎉 Your guess was perfect! Excellent Job! 🎉")
            break  # Ends the round and asks if they want to play again

        elif Userchoice < target:
            print("📉 Your guess is smaller than the target. Try a bigger number.")

        else:
            print("📈 Your guess is greater than the target. Try a smaller number.")

    # Ask the player if they want to continue playing
    play_again = input("\n🔄 Do you want to play again? (Y/N): ").strip().upper()
    if play_again != "Y":
        print("Thanks for playing! See you next time. 👋")
        break  
print("Take care, keep playing!\nGoodbye!!!!")
print("----------------- GAME OVER ---------------")