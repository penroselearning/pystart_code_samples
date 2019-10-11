import random

football_teams = ['Brazil', 'Argentina',
                'Germany', 'Italy', 'France', 'England', 'Uruguay',
                'Portugal', 'Spain', 'Sweden', 'Belgium', 'Croatia']

group1=[]
group2=[]

football_teams_2 = football_teams.copy()

for x in range(len(football_teams)):
    team = random.choice(football_teams_2)
    football_teams_2.remove(team)

    if len(group1) == len(football_teams)/2 :
        group2.append(team)
    else:
        group1.append(team)


print("Group 1")
print('-'*30)
for t in group1:
    print(t)


print()
print("Group 2")
print('-'*30)
for t in group2:
    print(t)

