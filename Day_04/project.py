import random

print("The game begins")
who_wins = ""
computer_choice = random.randint(0,2)
player_choice = int(input('''
Rock: 1
Paper: 2
Scissors: 3
Your decision: '''))

choices = ["rock","paper","scissors"]

#if player wins:
if (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0) or (player_choice == 3 and computer_choice == 1):
    who_wins = "User"
#if equal
elif (player_choice-1 == computer_choice):
    who_wins = "Equal"
#If cpu wins
else:
    who_wins = "Computer"

print(f"Your choice was: {choices[player_choice-1]}")
print(f"The computer choice was: {choices[computer_choice]}")
print(f"The winner of the game is: {who_wins}")