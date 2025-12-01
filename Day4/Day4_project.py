# Day 4 project: Rock, Paper, Scissors Game
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
pick_list = ["Rock", "Paper","Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice, try again!")
else:
    print(choice_list[user_choice])
    print("You chose: " + pick_list[user_choice] + "\n")
    computer_choice = random.randint(0, 2)
    print("Computer chose: " + pick_list[computer_choice])
    print(choice_list[computer_choice])
    
if user_choice == computer_choice:
    print("It's a draw! You both chose " + pick_list[user_choice])
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win! " + pick_list[user_choice] + " beats " + pick_list[computer_choice])
else:
    print("You lose! " + pick_list[computer_choice] + " beats " + pick_list[user_choice])
    