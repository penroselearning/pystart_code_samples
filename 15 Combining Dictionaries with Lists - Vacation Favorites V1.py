vacations = {'Vienna' : [2010,'Austria','Schönbrunn Palace', 'Apple Strudel']}

print(f'{"City":10} {"Year of Visit":13} {"Country":15} {"Favorite Spot":25} {"Favorite Food":25}')
print('-'*80)

for city,info in vacations.items():
  print(f'{city:10} {info[0]:13} {info[1]:15} {info[2]:25} {info[3]:25}')