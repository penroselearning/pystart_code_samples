name = "David Miller"

print(name)

# Using Slices to Extract the First 5 Characters
firstname=name[0:5:1]
# Start at 0th Index
# Stop at 5th Index
# Take Steps of 1

print(f'{firstname} is the first 5 letters in the name')

# The Same Result can also be achieved with the below code
firstname=name[:5:]
# If Start is left blank, it starts from 0th Index
# If Stop is left blank, it will go upto to last character
# If Step is left blank, it takes 1 Step

print(f'{firstname} is the first 5 letters in the name')

letters=name[0:-1]
print(f'{letters} is the name with Minus the last 1 Letter')