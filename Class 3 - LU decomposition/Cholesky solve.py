import mylibrary as lib
from math import sqrt

def Chol_dec(A):
    #function that performs the Cholesky decomposition on A and returns (L and T_transpose superimposed matrix where the diagonal of both are same).


    #IF NOT SYMMETRIC, EXIT.
    if lib.check_symmetry(A) == False:
        print('Non symmetric!')
        return None

    n = len(A)

    for row in range(n):
        for col in range(row,n):
            
            if row == col:
                sum = 0
                for i in range(row):
                    sum += (A[row][i] ** 2)
                A[row][row] = sqrt(A[row][row] - sum)
            else:
                sum = 0
                for i in range(row):
                    sum += (A[row][i] * A[i][col])
                A[row][col] = (A[row][col] - sum) / A[row][row]
                A[col][row] = A[row][col]

    return A

def forward_backward_cholesky(A,B):
    if A is None:
        print('Cholesky decomposition failed!')
        return None
    
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append((B[i][0]-sum)/ A[i][i]) #???!!! the / A[i][i] is unnecessary

    X = Y
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]

    for i in range(n):
        X[i] = [X[i]]
    
    return X

def solve_Cholesky(A,B): 
    #solves AX = B using cholesky Decomposition

    A = Chol_dec(A)
    if A is None:
        print('Cholesky Solve not possible!')
        return None

    
    return forward_backward_cholesky(A,B)

A1 = [[4,12,-16],[12,37,-43],[-16,-43,98]]
A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A2 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]

lib.print_mat(solve_Cholesky(A1,B))