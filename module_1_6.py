my_dict = {'Vera': 1999, 'Sasha': 1988, 'Max': 1977}
print(my_dict)

name = my_dict['Vera']
new_name = my_dict['Kris'] = 1998
print(name, new_name)

my_dict.update({'Lera': 1987,
                'Lexi': 1999})

del my_dict['Max']
print(my_dict.get('Max', 'Delete value: 1977'))

print(my_dict, "\n")



my_set = {'meow', 'meow', 123.2, False, False, (1, 2), 4, 4}
print(my_set )

my_set.update('mm',
              (988, 888))
my_set.discard(False)
print(my_set)








