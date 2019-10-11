
# Shopping Cart

shopping_cart = {'eggs':3.50,
'milk':4.50,
'cheese':3.75,
'yoghurt':2.75,
'butter':3.00,
'more cheese':1.75}

shopping_cart.update({'ketchup':4.50})

shopping_cart.update({'milk':4.75})

total_bill = 0

print("Final Shopping Cart")
print('-'*30)

for goods,price in shopping_cart.items():
  total_bill += price
  print(f'{goods.title():15} ${price}')

print('-'*30)
print(f'{"Total Bill":15} ${total_bill}')

shopping_cart.pop('cheese')


print(f'{number} x {x+1} = {number * (x+1)}')