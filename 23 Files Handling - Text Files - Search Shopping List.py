# Searching inside a Text File

search_item = input("Search Shopping List for: ").title()

if search_item in open('shoppinglist.txt').read():
  print(f"Yes,{search_item} is in the list")
else:
  print(f"No,{search_item} is not in the list")