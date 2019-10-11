shopping_list = ['Eggs', 'Brown Bread', 'Apple Juice', 'Strawberries', 'Cookies']

print('-' * 30)
print("Shopping List")
print('-' * 30)
for shopping_item in shopping_list:
    print(shopping_item)
print('-' * 30)

item = input("Enter a New Shopping List Item").title()
shopping_list.append(item)  # Adds an Item to the List

print('-' * 30)
print("Updated Shopping List after Adding New Item")
print('-' * 30)
for shopping_item in shopping_list:
    print(shopping_item)

print('-' * 30)

item = input("Enter Item you wish to Remove from your List").title()
shopping_list.remove(item)  # Removes Item from the List if it Exists

print('-' * 30)
print("Updated Shopping List after Removing an Item")
print('-' * 30)
for shopping_item in shopping_list:
    print(shopping_item)

print('-' * 30)