def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    print (result)
    return result


matrix1 = [[2, -2, -4], [-1, 3, 4], [1, -2, -3]]
matrix2 = [[2, -2, -4], [-1, 3, 4], [1, -2, -3]]


multiply_matrices(matrix1, matrix2)