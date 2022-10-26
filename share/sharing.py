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

def LU_dec(A):
    

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

def mat_makeSDD(A,B):

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

def solve_GS(A,B,tolerance):
    n = len(A)

    A,B= mat_makeSDD(A,B)
    if A is None:
        print('matrix cannot be made strictly diagonally dominant')
    

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
            if abs((temp) - (X[i][0])) > tolerance:
                flag = 0
            X[i][0] = temp
        if flag == 1:
            return X,steps + 1
    return None,100

def solve_Jacobi(A,B,tolerance):

    A,B= mat_makeSDD(A,B)
    if A is None:
        print('matrix cannot be made strictly diagonally dominant')

    n = len(A)
    currX = [0] * n
    newX = currX[:]
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j: sum += (A[i][j] * currX[j])
        newX[i] = (B[i][0] - sum) / A[i][i]
    newX,currX = currX[:],newX[:]
    steps = 1
    while steps < 150:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j: sum += (A[i][j] * currX[j])
            newX[i] = (B[i][0] - sum) / A[i][i]

        flag = 1
        for i in range(n):
            if abs(newX[i]-currX[i]) > tolerance:
                flag = 0
                steps += 1
                currX = newX[:]
                break
        if flag == 1:
            for i in range(n):
                newX[i] = [newX[i]]
            return newX, steps
    return None, steps

def Chol_dec(A):
    if check_symmetry(A) == False:
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
def forwardbackward_cholesky(A,B):
    if A is None:
        print('Cholesky decomposition failed!')
        return None
    Y = []
    n = len(B)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += (A[i][j] * Y[j])
        Y.append((B[i][0]-sum)/ A[i][i])
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i + 1, n):
            sum += (A[i][j] * Y[j])
        Y[i] = (Y[i] - sum) / A[i][i]
    return Y
def solve_Cholesky(A,B): 
    return forwardbackward_cholesky(Chol_dec(A),B)


def poly_fit(X,Y,k):

    n = len(X)

    A = [[0]*(k+1) for i in range(k+1)]

    A[0][0] = n
    for i in range(1,(2 * k) + 1):
        sum = 0
        for j in range(n):
            sum += (X[j]**i)
        if i <= k:
            row = 0
            col = i
            while col >= 0:
                A[row][col] = sum
                col -= 1
                row += 1
        else:
            row = i - k
            col = k
            while row <= k:
                A[row][col] = sum
                col -= 1
                row += 1

    B = []
    sum = 0
    for i in range(n):
        sum += Y[i]
    B.append([sum])
    for i in range(1,k+1):
        sum = 0
        for j in range(n):
            sum += (X[j]**i)*Y[j]
        B.append([sum])


    px = lib.solve_GJ(A,B)
    
    for j in range(len(px)):
        px[j] = px[j][0]

    return px