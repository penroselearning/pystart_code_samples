from fractions import Fraction

numerator = int(input("Enter Numerator"))
denominator = int(input('Enter Denominator'))

least_fraction=Fraction(numerator,denominator)

print('-'*30)
print(f'''The Least Fraction of {numerator}/{denominator} is {least_fraction} ''')