zoo = {'elephant': {'number': 4 ,'eyes': 2, 'legs': 4, 'tails': 1},              
        'spider': {'number': 10 , 'eyes': 5, 'legs': 8},
        'cyclops': {'number': 2 , 'eyes': 1, 'legs': 2, 'arms':2}}
def partCount(animals, part):
  parts = 0
  for i,j in animals.items():
    parts += (j.get(part,0))*(j.get('number',1))
  return parts

print('Number of parts in zoo:')
print(' - Eyes           ' + str(partCount(zoo, 'eyes')))
print(' - Legs           ' + str(partCount(zoo, 'legs')))
print(' - Tails          ' + str(partCount(zoo, 'tails')))
print(' - Arms           ' + str(partCount(zoo, 'arms')))
print(' - Wings          ' + str(partCount(zoo, 'wings')))
