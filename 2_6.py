key = int(input('Введите чисkо от 3 до 20: '))
k = 0

for i in range(1, 10):
    for k in range (1, 10):
        if key % (i + k) == 0 and i < k and i != k:
            result = [i, k]

            print(result)
