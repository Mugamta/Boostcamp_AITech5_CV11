def matrix_multiply(mat1, mat2):  # 2 x 2 행렬의 곱을 리턴
    return [[(mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % 1000000,
             (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % 1000000],
            [(mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % 1000000,
             (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % 1000000]]


def matrix_pow(exponent, matrix):
    if exponent > 1:
        res = matrix_pow(exponent // 2, matrix)
        if exponent % 2 == 1:
            return matrix_multiply(matrix, matrix_multiply(res, res))
        return matrix_multiply(res, res)
    return matrix


def fibonacci(n):
    matrix = [[1, 1], [1, 0]]
    return matrix_pow(n, matrix)[1][0]


print(fibonacci(int(input())))