import mylibrary as lib

def forward_backward_cholesky(A,B):
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append((B[i][0]-sum)/A[i][i])

    X = Y
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * X[j])
        X[i] = (Y[i] - sum) / A[i][i]

    for i in range(n):
        X[i] = [X[i]]

    return Y

def Cholesky_solve(A,B): 
    #solves AX = B using cholesky Decomposition

    A = lib.Chol_dec(A)
    if A is None:
        print('Cholesky Solve not possible!')
        return None

    # Finding Y from (L)(Y) = B by forwarwd substitution

    # Finding X from (Lt)(X) = (Y) by backward substitution
    
    return forward_backward_cholesky(A,B)

A1 = [[4,12,-16],[12,37,-43],[-16,-43,98]]
A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A2 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]

lib.print_mat(Cholesky_solve(A1,B))