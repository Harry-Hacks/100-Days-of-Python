# Day 3 project: Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Where do you want to go first? Type 'left' or 'right'\n")
choice1 = choice1.lower()
if choice1 == "left":
    choice2 = input("You turn left and come to a river, do you want to 'wait' or 'swim'?\n")
    choice2 = choice2.lower()
    if choice2 == "swim":
        print("You were attacked by a trout. Game over, better luck next time.")
        exit()
    elif choice2 == "wait":
        choice3 = input("Your patience has paid off and a boat has come to take you across. You arrive at an island with 3 doors: one red, one yellow and one blue. Which door do you choose?\n")
        choice3 = choice3.lower()
        if choice3 == "red":
            print("Uh oh you were burned by fire. Game over, better luck next time.")
            exit()
        elif choice3 == "blue":
            print("Aw rats, you were eaten by beasts. Game over, better luck next time.")
            exit()
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure!")
        else:
            print("You chose a door that doesn't exist. Game over, better luck next time.")
            exit()
else:
    print("You fell into a hole. Game over, better luck next time.")
    exit()
