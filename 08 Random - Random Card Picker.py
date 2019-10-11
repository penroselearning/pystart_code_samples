import random

card_suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_face = [2, 3, 4, 5, 6, 7, 8, 9, 10,'Ace','Jack','Queen','King']

# Stores a Random Number between 1 to 10
chosen_card_suit = random.choice(card_suit)
chosen_card_face = random.choice(card_face)

# Prints the Chosen Random Card
chosen_card = print(f'The chosen Card is {chosen_card_face} of {chosen_card_suit}')