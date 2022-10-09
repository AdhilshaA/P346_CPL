

def mat_makeSDD(A,B):
    #makes a strictly diagonally dominant matrix A after row swaps on A and the same row operations on B. returns both.

    n = len(A)
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i:
                sum += abs(A[i][j])
        if abs(A[i][i]) > sum:
            continue
        else:
            curr = i + 1
            flag = 0
            while curr < n:
                sum = 0
                for j in range(n):
                    if j != i:
                        sum += abs(A[curr][j])
                if abs(A[curr][i]) > sum:
                    flag = 1
                    break
                else:
                    curr += 1
            if flag == 0:
                return None,None
            else:
                A[i],A[curr] = A[curr],A[i]
                B[i],B[curr] = B[curr],B[i]
    return A,B

def Jacobi_solve(A,B,tolerance):

    #diagonally dominant
    A,B = mat_makeSDD(A,B)

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
    while steps < 100:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j: sum += (A[i][j] * X1[j])
            X2[i] = (B[i][0] - sum) / A[i][i]
        print(X2,X1)
        flag = 1
        for i in range(len(A)):
            if abs((X2[i]) - (X1[i])) > tolerance:
                flag = 0
                steps += 1
                X1 = X2[:]
                break
        if flag == 1:
            return X2, steps
    print('After more than 100 iterations, it is not solved!')
    return None, steps    
A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A1 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]
B2 = [[13],[6],[15]]
A2 = [[2,3,1],[1,1,1],[3,2,2]]
A3 = [[4.0, 0.0, 4.0, 10.0, 1.0], [0.0, 4.0, 2.0, 0.0, 1.0], [2.0, 5.0, 1.0, 3.0, 13.0], [11.0, 3.0, 0.0, 1.0, 2.0], [3.0, 2.0, 7.0, 1.0, 0.0]]
B3 = [[20.0], [15.0], [92.0], [51.0], [15.0]]
solution,steps = Jacobi_solve(A3,B3,0.000001)
print('The solution is {}, acheived after {} steps'.format(solution,steps))