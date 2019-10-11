number1 = int(input("Enter a Number of your choice:\n"))
number2 = int(input("Enter a Second Number :\n"))

# The below code multiplies the '-' dash character 30 times
print('-'*30)

sum         = number1 + number2
difference  = number1 - number2
product     = number1 * number2
division    = number1 / number2
modulus     = number1 % number2
quotient    = number1 // number2
exponent    = number1**number2

print(f"The sum of the numbers is {sum} ")
print(f"The difference of the numbers is {difference} ")
print(f"The product of the numbers is {product} ")
print(f"The division of the numbers is {division} ")
print(f"The remainder / modulus of the numbers is {modulus} ")
print(f"The quotient of the numbers is {quotient} ")
print(f"{number1} raised to the Power of {number2} is {exponent:,} ")