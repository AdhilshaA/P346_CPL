import mylibrary as lib

def GS_solve(A,B,tolerance):
    n = len(A)

    #symmetric and positive definite (ztranspose*A*z > 0 where z is any vector)
    if lib.check_pos_definite(A) == False:
        print('Not postive definite matrix!\nGauss-Seidel solve not possible!')
        return None
    
    #diagonally dominant
    

    X = list([0] for i in range(n)) #guess
    
    for steps in range(100):
        flag = 1
        for i in range(n):
            sum = 0
            for j in range(i):
                sum += (A[i][j] * X[j][0])
            for j in range(i+1,n):
                sum += (A[i][j] * X[j][0])
            temp = (B[i][0] - sum) / (A[i][i])
            if abs(abs(temp) - abs(X[i][0])) > tolerance:
                flag = 0
            X[i][0] = temp
        if flag == 1:
            return X,steps + 1
    print('Eqn not solved after 100 steps')
    return None,100

A = [[4,-1,1],[4,-8,1],[-2,1,5]]
A1 = [[4,-1,1],[-2,1,5],[4,-8,1]]
B = [[7],[-21],[15]]
A2 = [[4,1,-1,1],[1,4,-1,-1],[-1,-1,5,1],[1,-1,1,3]]
B2 = [[-2],[-1],[0],[1]]
solution,steps = GS_solve(A2,B2,0.00001)
print('The solution is {}, acheived after {} steps'.format(solution,steps))

