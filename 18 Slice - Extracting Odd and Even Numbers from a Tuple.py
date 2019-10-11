## Slices with Tuples

numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
print(numbers)

odd = numbers[0::2]
# Start from 0th Index
# Stop is Blank, therefore extracts till the end
# Step is 2, therefore extracts each alternate
print(f'{odd} are the Odd Numbers')

even = numbers[1::2]
# Start from 1st Index
# Stop is Blank, therefore extracts till the end
# Step is 2, therefore extracts each alternate
print(f'{even} are the Even Numbers')