from datetime import datetime

random_date = '22-Oct-1983'
print(f'Provided Date in String Format: {random_date}')

# Print the String in Date Format
new_date=datetime.strptime(random_date,'%d-%b-%Y')
print(f'Converted into Date Format: {new_date}')