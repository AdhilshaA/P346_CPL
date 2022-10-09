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