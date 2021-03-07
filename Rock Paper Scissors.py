# Creating Rock Paper Scissors using Python

""" We'll be taking the move in the player, and the program will
randomly select its move. The first one to reach the score of 3 wins the game."""

import random


user_wincount = 0
computer_wincount = 0
play = False

print("Rock Paper Scissors")
while not play:
    computer = ['rock', 'paper', 'scissor']
    computer_move = random.choice(computer)
    move = str(input("Enter move: ")).lower()
    if move == computer_move:
        print("Tie")
    elif move == "rock":
        if computer_move == "paper":
            print(f"You lose, {computer_move} covers {move}.")
            computer_wincount += 1
        else:
            print(f"You win, {move} smashes {computer_move}.")
            user_wincount += 1
    elif move == "paper":
        if computer_move == "scissor":
            print(f"You lose, {computer_move} cuts {move}.")
            computer_wincount += 1
        else:
            print(f"You win, {move} covers {computer_move}.")
            user_wincount += 1
    elif move == "scissor":
        if computer_move == "rock":
            print(f"You lose, {computer_move} smashes {move}.")
            computer_wincount += 1
        else:
            print(f"You win, {move} cuts {computer_move}.")
            user_wincount += 1
    else:
        print("Wrong input. ")

    if computer_wincount == 3:
        play = True
    elif user_wincount == 3:
        play = True
    else:
        continue

if computer_wincount == 3:
    print("\nGame Over! Better Luck next time!")
else:
    print("\nYou win! Keep it up!")
