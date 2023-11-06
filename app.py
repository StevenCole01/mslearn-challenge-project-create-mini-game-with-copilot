import random

options_list = ["rock","paper","scissors"]
continue_game = True
wins = 0
rounds = 0

while (continue_game):
    # get user input and validate it is a valid option from the options_list
    user_input = input("Enter rock, paper, or scissors: ")
    while (user_input not in options_list):
        print("Invalid input. Please enter rock, paper, or scissors.")
        user_input = input("Enter rock, paper, or scissors: ")

    # get computer choice
    computer_choice = random.choice(options_list)

    # determine winner 
    if (user_input == computer_choice):
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors"):
        print("You win!")
        wins = wins + 1
    elif (user_input == "paper" and computer_choice == "rock"):
        print("You win!")
        wins = wins + 1
    elif (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
        wins = wins + 1
    else:
        print("You lose!")
    
    rounds = rounds + 1

    # ask user if they want to play again
    play_again = input("Would you like to play again? (y/n) ")
    while (play_again != "y" and play_again != "n"):
        print("Invalid input. Please enter y or n.")
        play_again = input("Would you like to play again? (y/n) ")

    if (play_again == "n"):
        continue_game = False

# print number of wins and rounds played
print("You won", wins, "out of", rounds, "rounds.")
