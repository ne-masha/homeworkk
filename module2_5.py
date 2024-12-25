def get_matrix(n, m, value):
    matrix = []
    for str_count in range(n):
        matrix.append([])
        for str_count2 in range(m):
            matrix[str_count].append(value)
    print(matrix)
    return matrix

result = get_matrix(2,2, 10)
print(result)

