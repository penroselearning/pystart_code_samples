# Writing Data to a CSV File

import csv
import os.path
from datetime import datetime

print("Swimming Academy - Registration")
print("-" * 20)

filename = 'students.csv'
file_exists = os.path.isfile(filename)

fieldnames = ['name', 'date_of_birth', 'school', 'grade', 'registration_date']
today = datetime.now()

with open("students.csv", 'w') as csvfile:
    csvEntry = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if file_exists is False:
        csvEntry.writeheader()

    csvEntry.writerow({
        'name': input('Enter Name:\n'),
        'date_of_birth': input('Enter Date of Birth:\n'),
        'school': input('Enter School:\n'),
        'grade': input('Enter Grade:\n'),
        'registration_date': today.strftime('%d-%b-%Y')
    })
print("Student Record has been saved")