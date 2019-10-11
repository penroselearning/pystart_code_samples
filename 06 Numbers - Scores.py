# Increasing and Decreasing the Numeric Value of the Variables

score = 0

# The below code increases the score value by 10
score = score+10

# The above code can also be written as
score += 10

print(f'The Score is {score}')

# The below code decreases the score value by 10
score = score-10

# The above code can also be written as
score -= 10

print(f'The Score is {score}')



weather = "raining"
if weather == '"raining":
    print("Take your Umbrella")
else:
    print("Wear your Cap")



if score >= 90:
  print("Grade A")
elif score >= 75 and score < 90:
  print("Grade B")
elif score >=50 and score < 75:
  print("Grade D")
elif score >=35 and score < 50:
  print("Grade E")
elif score <35:
  print("Fail")