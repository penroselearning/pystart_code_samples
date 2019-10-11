students = [('Sandra', 15),
            ('Hashim', 12),
            ('Hassan', 14),
            ('Keith', 15),
            ('Ellie', 16)]

print(f'{"Name":10} {"Age"}')
print('-' * 20)

for student in students:
    print(f'{student[0]:10} {student[1]}')