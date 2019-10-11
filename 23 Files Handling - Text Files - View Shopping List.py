print("Your Shopping List")
print("-"*20)
with open("shoppinglist.txt",'r') as file:
  print(file.read())