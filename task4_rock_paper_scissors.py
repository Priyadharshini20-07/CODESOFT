# task4_rock_paper_scissors.py

import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print(" Rock-Paper-Scissors Game")

while True:
    print("\nOptions: rock, paper, scissors")
    user_choice = input("Enter your choice (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print(" Game Over!")
        print(f"Final Score - You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in options:
        print(" Invalid choice! Try again.")
        continue

    computer_choice = random.choice(options)
    print(f" You chose: {user_choice}")
    print(f" Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(" You win this round!")
        user_score += 1
    else:
        print(" You lose this round!")
        computer_score += 1
