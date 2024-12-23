my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0

while index_ < len(my_list):
    num = my_list[index_]
    index_ = index_ + 1 #берем число из списка чей инлекс (x+1)
    if num == 0:
        continue
    elif num < 0:
        break
    elif index_ == len(my_list):
        print(num)
    else:
        print(num)

