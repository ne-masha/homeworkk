print("Введите три числа: ")

first_num = input()
second_num = input()
third_num = input()

if first_num == second_num == third_num:
    print(3)
elif first_num == second_num or second_num == third_num or first_num == third_num:
    print(2)
else:
    print(0)