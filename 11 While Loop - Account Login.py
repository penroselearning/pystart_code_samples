ACCOUNT_PIN=1234

pin=int(input("Enter your Account Pin:\n"))

while pin != ACCOUNT_PIN:
  pin=int(input("Sorry, Incorrect Pin. Please Re-Enter:\n"))

print('-'*30)
print("Welcome to your Account")

# As per above example, the user prompt will keep appearing until the correct password 1234
# has been entered.
# Only if the Password has been entered correctly, it will exit the While Loop
