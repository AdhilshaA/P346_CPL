import mylibrary as lib

def LU_dec(A):

    #leading sub matrix nonzero, pivot
    
    n = len(A)
    if n != len(A[0]):
        print('Not square!')
        return None
    for j in range(n):
        for i in range(1,n):
            if i <= j:
                sum = 0
                for k in range(0,i):
                    sum += (A[i][k] * A[k][j])
                A[i][j] = A[i][j] - sum
            else:
                sum = 0
                for k in range(0,j):
                    sum += (A[i][k] * A[k][j])
                A[i][j] = (A[i][j] - sum) / A[j][j]

    return A

def forward_backward_LU(A,B):
    if A is None:
        print('LU decomposition failed!')
        return None
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append(B[i][0]-sum)
    X = Y[:]
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]
    for i in range(n):
        X[i] = [X[i]]

    return X

def LU_solve(A,B):
    return forward_backward_LU(LU_dec(A),B)

A1 = [[4,12,-16],[12,37,-43],[-16,-43,98]]
A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A2 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]

lib.print_mat(LU_solve(A1,B))

