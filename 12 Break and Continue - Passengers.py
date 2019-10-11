passengers = []

while True:
    passengers.append(input("Enter Name of Passenger:\n").strip())

    quit = input("Press Enter to add a New Passenger or any other key to exit")

    if quit != '':
        break

print()
print("Passenger List")
print('-' * 30)
for passenger in passengers:
    print(passenger)