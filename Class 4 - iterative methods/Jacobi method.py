def Jacobi_solve(A,B,tolerance):

    #diagonally dominant

    n = len(B)
    X1 = [0] * n
    X2 = X1[:]
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j: sum += (A[i][j] * X1[j])
        X2[i] = (B[i][0] - sum) / A[i][i]
    X2,X1 = X1[:],X2[:]
    steps = 1
    while steps < 50:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j: sum += (A[i][j] * X1[j])
            X2[i] = (B[i][0] - sum) / A[i][i]

        flag = 1
        for i in range(len(A)):
            if (((abs(X2[i]) - abs(X1[i])) / abs(X1[i])) * 100) > tolerance:
                flag = 0
                steps += 1
                X1 = X2[:]
                break
        if flag == 1:
            return X2, steps
    print('After more than 50 iterations, it is not solved!')
    return None, steps    
A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A1 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]
B2 = [[13],[6],[15]]
A2 = [[2,3,1],[1,1,1],[3,2,2]]
solution,steps = Jacobi_solve(A,B,0.0001)
print('The solution is {}, acheived after {} steps'.format(solution,steps))