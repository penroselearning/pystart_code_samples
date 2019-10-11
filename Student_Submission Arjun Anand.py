SAT = int(input("Enter your SAT score\n"))

if SAT > 1600:
    print("You think you're smart?!!")
elif SAT == 1600:
    print("Wow you've aced the test!!! Acing the SAT is extremely hard so feel proud")
elif SAT >= 1500:
    print("Good job you've done well on the SAT")
elif SAT >= 1400:
    print("Nice, but you should try again to get a better score")
elif SAT >= 1300:
    print("You should try the SAT again")
elif SAT >= 1200:
    print("Study harder next time")
elif SAT >= 1100:
    print("Did you even study")
else:
    print("You're not ready for a job or any college")