## We had created a Restaurant Menu while we learned IF Statements.
## We will replicate it using Dictionaries.

print("Bake Shop")
print("-" * 30)

menu = {'Brownie': 2.5,
        'Croissant': 3,
        'Choco Cookie': 2.75}

for food, price in menu.items():
    print(f'{food:15} USD {price}')

bill = 0

order = input("Kindly place your Order:\n").title()

if order in menu.keys():  # Checks if the Ordered Item is found in the Dictionary Keys

    for menu, price in menu.items():  # We use a Loop to run through the Dictionary Items
        if menu == order:  # For the Ordered Item
            bill += price  # The Price is added to the Bill

else:
    print(f'Sorry, Wrong Order!! We do not sell {order}')

quantity = int(input(f'How Many {order}s do you wish to Order?\n'))

print('-' * 30)
print(f'The Total Bill Amount is $ {bill * quantity}')


player = {'Ronaldo' : [34,'Portugal','Juventus']}

for name,info in player.items():
  print(f'{name:12} {info[0]} {info[1]} {info[2]}')





