import random

fantasy_boxers = ['Floyd Mayweather', 'Muhammad Ali', 'Manny Pacquiao',
                  'Mike Tyson', 'George Freeman', 'Amir Khan', 'Vijender Singh']

matches = 6

print(f'Fantasy Boxing Matches')
print('-' * 30)

while matches > 0:
    boxer1 = random.choice(fantasy_boxers)
    boxer2 = random.choice(fantasy_boxers)

    if boxer1 == boxer2:
        continue
    else:
        print(f"{boxer1} versus {boxer2}")
        matches -= 1