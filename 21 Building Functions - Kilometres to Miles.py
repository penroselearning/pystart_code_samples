def km_to_miles(kilometer):
    miles = round(kilometer * 0.621371, 2)
    print(f'{kilometer} kilometer(s) equals {miles:,} miles')


print("Kilometer to Miles Convertor")
print('-' * 30)

km = float(input('Enter Kilometers:\n'))

km_to_miles(kilometer=km)