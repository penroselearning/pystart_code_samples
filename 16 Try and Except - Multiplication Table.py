print('Multiplication Table')
print('-'*30)

while True:
  try:
    number = int(input("Enter a Number of Your Choice:\n"))
  except:
    print("Sorry! You have not entered a Number")
  else:
    for x in range(10):
      print(f'{number} x {x+1} = {number * (x+1)}')
    break