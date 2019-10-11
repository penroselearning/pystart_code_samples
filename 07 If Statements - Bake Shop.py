# Penrose Bake Shop

brownie=5
croissant=3
chocochip=2.5

print(f'''Menu
------------------------------
Brownie           - $ {brownie}
Croissant         - $ {croissant}
Choco Cookie      - $ {chocochip}''')

print('-'*30)

bill = 0

order = input("Kindly place your Order:\n").lower()
quantity = int(input(f'How Many {order}s do you wish to Order?\n'))

if order == 'brownie':
  bill+=brownie
elif order =='croissant':
  bill+=croissant
elif order == 'choco cookie':
  bill+=chocochip
else:
  print(f'Sorry, Wrong Order!! We do not sell {order}')


print('-'*30)
print(f'The Total Bill Amount is $ {bill*quantity}')