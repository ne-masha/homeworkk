immutable_var = (1, True, "Pear", 741)
print(immutable_var)

#immutable_var[1] = False
#print(immutable_var)
#при выполнении закомментированной части кода произошла ошибка, тк в кортеж нельзя внести изменение такого типа

mutable_list = ["pearl", 852, False, 96.3]
mutable_list[1] = 123
print(mutable_list)
