import random

print("Welcome to the Mental Math Game")
print('-' * 30)

operations=['+','-']

while True:
    try:
        rounds=int(input('How many rounds would you like to play?\n'))
        print('-' * 15)

    except ValueError:
        print("Enter a Number")

    else:
        for x in range(rounds):
            n1 = random.randint(1, 25)
            n2 = random.randint(1, 25)
            operation = random.choice(operations)

            if operation == '+':
                question = (f'{n1} + {n2} = ')
                qanswer = n1 + n2
            else:
                qanswer = n1 - n2
                question = (f'{n1} - {n2} = ')
            try:
                answer = int(input(question))
            except:
                print(f'Incorrect. Correct Answer is {qanswer}\n')
            else:
                if answer == qanswer:
                    print('Correct, well done\n')
                else:
                    print(f'Incorrect. Correct Answer is {qanswer}\n')
        break