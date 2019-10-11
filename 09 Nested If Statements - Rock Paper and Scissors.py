print('''

Lets Play the Rock,Paper & Scissors Game''')
print('-' * 30)

import random

game = ['rock', 'paper', 'scissors']

computer = random.choice(game)

player = input("What is your choice - Rock,Paper or Scissors? \n").lower()

if computer == 'rock':

    if player == computer:
        print("It's a Draw")
    elif player == 'paper':
        print("You Won")
    elif player == "scissors":
        print(f"You Lost. The Computer chose {computer}")
    else:
        print("Sorry!! You have entered a wrong choice. Restart the Game")

elif computer == 'paper':

    if player == computer:
        print("It's a Draw")
    elif player == 'scissors':
        print("You Won")
    elif player == "rock":
        print(f"You Lost. The Computer chose {computer}")
    else:
        print("Sorry!! You have entered a wrong choice. Restart the Game")

elif computer == 'scissors':

    if player == computer:
        print("It's a Draw")
    elif player == 'rock':
        print("You Won")
    elif player == "paper":
        print(f"You Lost. The Computer chose {computer}")
    else:
        print("Sorry!! You have entered a wrong choice. Restart the Game")