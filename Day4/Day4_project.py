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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
elif user == 0:
    print(rock)
    if computer == 0:
        print("Computer chose:\n")
        print(rock)
        print("It's a draw")
    elif computer == 1:
        print(paper)
        print("Computer chose:\n")
        print("You lose")
    else:
        print(scissors)
        print("Computer chose:\n")
        print("You win")
elif user == 1:
    print(paper)
    if computer == 0:
        print("Computer chose:\n")
        print(rock)
        print("You win")
    elif computer == 1:
        print("Computer chose:\n")
        print(paper)
        print("It's a draw")
    else:
        print(scissors)
        print("Computer chose:\n")
        print("You lose")
elif user == 2:
    print(scissors)
    if computer == 0:
        print(rock)
        print("Computer chose:\n")
        print("You lose")
    elif computer == 1:
        print(paper)
        print("Computer chose:\n")
        print("You win")
    else:
        print(scissors)
        print("Computer chose:\n")
        print("It's a draw")
        