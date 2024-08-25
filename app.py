# Create a multiplayer rock-paper-scissors game where the player competes against the computer.
# The game should have the following features:
# - The player can choose one of the three options: rock, paper, or scissors.
# - The computer randomly chooses one of the three options.
# - The game should determine the winner of each round based on the standard rock-paper-scissors rules.
# - The player should be informed of the outcome of each round.
# - The player can choose to play again after each round.
# - The game should keep track of the player's score.
# - The game should handle invalid input from the player.

# Code Structure:
# 1. Define a function to get the player's choice.
# 2. Define a function to get the computer's choice.
# 3. Define a function to determine the winner of a round.
# 4. Define a function to play the game.
# 5. Implement the main game loop.

# Additional Notes:
# - Use lowercase for all input and output to avoid case sensitivity issues.
# - Provide clear and informative messages to the user.
# - Consider adding features like a scoring system or a timer.

import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_game()