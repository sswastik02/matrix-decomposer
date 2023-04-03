import numpy as np

def lDecomposition(matrix):
    n = len(matrix)
    lower = np.zeros((n, n))
 
    # Lower Triangular
    for j in range(i, n):
        if i == j:
            lower[i][i] = 1  # Diagonal as 1
        else:
            sum = 0
            for k in range(i):
                sum += (lower[j][k] * upper[k][i])
            lower[j][i] = (matrix[j][i] - sum) / upper[i][i]
 
    return upper
def uDecomposition(matrix):
    n= len(matrix)
    upper = np.zeros((n,n))
    
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (lower[i][k]*upper[k][j])
            upper[i][j] = matrix[i][j] - sum
    return upper
    
 
matrix = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])
n = len(matrix)
lower = lDecomposition(matrix)
upper = uDecomposition(matrix)

print("Lower Triangular\t\tUpper Triangular")
for i in range(n):
    for j in range(n):
        print(lower[i][j], end="\t")
    print("", end="\t")
    for j in range(n):
        print(upper[i][j], end="\t")
    print("")
