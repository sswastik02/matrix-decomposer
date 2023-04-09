import numpy as np

def uDecomposition(matrix):
    n = len(matrix)
    helper = np.zeros((n, n))
    upper = np.zeros((n, n))

    # Decomposition
    for i in range(n):
        # Upper Triangular
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (helper[i][k] * upper[k][j])
            upper[i][j] = matrix[i][j] - sum

        for j in range(i, n):
            if i == j:
                helper[i][i] = 1  # Diagonal as 1
            else:
                sum = 0
                for k in range(i):
                    sum += (helper[j][k] * upper[k][i])
                helper[j][i] = (matrix[j][i] - sum) / upper[i][i]

    return upper


def lDecomposition(matrix):
    n = len(matrix)
    lower = np.zeros((n, n))
    helper = np.zeros((n, n))

    # Decomposition
    for i in range(n):
        # Lower Triangular
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (lower[i][k] * helper[k][j])
            helper[i][j] = matrix[i][j] - sum

        for j in range(i, n):
            if i == j:
                lower[i][i] = 1  # Diagonal as 1
            else:
                sum = 0
                for k in range(i):
                    sum += (lower[j][k] * helper[k][i])
                lower[j][i] = (matrix[j][i] - sum) / helper[i][i]

    return lower
