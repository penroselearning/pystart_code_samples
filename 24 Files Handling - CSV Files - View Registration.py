import csv
import os.path

print("Swimming Academy - Registered List")
print("-" * 30)

fieldnames = ['name', 'date_of_birth', 'school', 'grade', 'registration_date']

with open("students.csv", 'r') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)

    students = list(csvReader)

    for student in students:
        print(f'{student["name"]:10} | {student["date_of_birth"]:15} | {student["school"]:25} | {student["grade"]:5} | {student["registration_date"]}')