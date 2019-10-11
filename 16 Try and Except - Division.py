print('Division')
print('-'*30)

while True:
  try:
    dividend = int(input("Enter a Dividend:\n"))
    divisor = int(input("Enter a Divisor:\n"))
  except ValueError:
    print("Sorry! You have not entered a Number")
  else:
    try:
      result = dividend/divisor
    except ZeroDivisionError:
      print("Division by Zero has an Undefined Value")
    else:
      print(f'The quotient is {result}')
      break