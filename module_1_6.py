my_dict={'Ann':1996, 'Alex':1973, 'Nadya':1979}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Ann'))
print('Not existing value: ', my_dict.get('Misha'))
my_dict['Nina']=1954
my_dict.update({'Olya':1950})
a=my_dict.pop('Ann')
print('Modified dictionary: ', my_dict)
print('Deleted value: ', a)

my_set={14, 'Кот', 14.1, 14, 'Кот', 'Осень'}
print('Set', my_set)
my_set.add('Зима')
my_set.add(1978)
my_set.remove(14.1)
print('Modified set: ', my_set)