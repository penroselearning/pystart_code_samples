vacations = {'Vienna' : [{'Year Visited':2011},
                       {'Country':'Austria'},
                       {'Favorite Spot':'Schönbrunn Palace'},
		                   {'Favorite Food':'Apple Strudel'}]}
print('-'*30)
for city,info in vacations.items():
  print(f'City  : {city}')

print(f'''
Year Visited     : {info[0]['Year Visited']}
Country 		 : {info[1]['Country']}
Favorite Spot    : {info[2]['Favorite Spot']}
Favorite Food    : {info[3]['Favorite Food']}
''')