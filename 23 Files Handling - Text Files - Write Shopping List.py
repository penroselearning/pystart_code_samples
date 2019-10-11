shopping_list=['Bread','Eggs','Orange Juice','Yoghurt','Cookies']

with open("shoppinglist.txt",'w') as file:
  sno=1
  for item in shopping_list:
    file.write(f'{sno}.{item}\n')
    sno+=1

print(f"{len(shopping_list)} item(s) have been saved in the Shopping List File")