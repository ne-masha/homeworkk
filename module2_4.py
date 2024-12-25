numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    is_primes = True
    if num == 1:
        continue
    for num_2 in numbers:
        if num_2 == 1 or num == num_2:
            continue
        elif num % num_2 == 0:
            num = False
            break
        else:
            num = is_primes
        if  num == True:
            num = primes
        else:
            num = not_primes

print('primes: ', primes)
print('not primes', not_primes)










