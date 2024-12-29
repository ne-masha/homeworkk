#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print()

#2
list_values = [True, 123, 'str']
dict_values = {'a': False, 'b': 321, 'c': 'hehe'}

print_params(*list_values)
print_params(**dict_values)

print()

#3
values_list_2 = [2.2, False]
print_params(*values_list_2, 42)



