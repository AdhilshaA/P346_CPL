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


def RK4_coupled(flist,x0,y0s,x1,h):
    x1 -= h/2 
    n = len(y0s) 
    k1 = [0]*n
    k2 = [0]*n
    k3 = [0]*n
    k4 = [0]*n
    tempys = [0]*n 
    datY = []
    for i in range(n):
        datY.append([y0s[i]])
    datX = [x0]
    while x0 < x1:
        for i in range(n):
            k1[i] = h*flist[i](y0s,x0)
        for i in range(n):
            tempys[i] = y0s[i] + (k1[i] / 2)
        for i in range(n):
            k2[i] = h*flist[i](tempys, (x0 + (h/2)))
        for i in range(n):
            tempys[i] = y0s[i] + (k2[i] / 2)
        for i in range(n):
            k3[i] = h*flist[i](tempys, (x0 + (h/2)))   
        for i in range(n):
            tempys[i] = y0s[i] + k3[i]
        for i in range(n):
            k4[i] = h*flist[i](tempys, (x0 + h))
        for i in range(n):
            y0s[i] += ((k1[i] + (2 * k2[i]) + (2 * k3[i]) + (k4[i])) / 6)
        x0 += h
        for i in range(n):
            datY[i].append(y0s[i])
        datX.append(x0)
    return datX, datY

def diff_shooting(fns,x0,y0,x1,y1,guess1,epsilon,h):    
    X,Y = RK4_coupled(fns,x0,[y0,guess1],x1,h)
    yend1 = Y[0][-1]
    if abs(yend1 - y1) < epsilon:
        return X,Y
    if yend1 < y1:
        guess1side = -1
    else :
        guess1side = 1

    guess2 = guess1 + 2   
    X,Y = RK4_coupled(fns,x0,[y0,guess2],x1,h)
    ye = Y[0][-1]
    if ye < y1:
        guess2side = -1
    else :
        guess2side = 1
    while guess1side * guess2side != -1:
        if abs(y1-ye) > abs(y1-yend1):
            guess2 = guess1 - abs(guess2-guess1)
        else:
            guess2 += abs(guess2-guess1)
        
        X,Y = RK4_coupled(fns,x0,[y0,guess2],x1,h)
        ye = Y[0][-1]
        if ye < y1:
            guess2side = -1
        else :
            guess2side = 1

    if guess1side == 1:
        guess1,guess2 = guess2,guess1

    i = 0
    while True:
        newguess = guess1 + (((guess2 - guess1)/(yend1 - ye))*(y1 - ye))
        i += 1
        X,Y = RK4_coupled(fns,x0,[y0,newguess],x1,h)
        yvalnew = Y[0][-1]

        if abs(yvalnew - y1) < epsilon:
            break
        if yvalnew < y1:
            guess1 = newguess
            yend1 = yvalnew
        else:
            guess2 = newguess
            ye = yvalnew
    return X, Y


def eigen_rayleigh(A,x0,epsilon):
    Akx0 = (A*x0)
    denom = (Akx0.dot(x0))
    Akx0 = (A*Akx0)
    num = (Akx0.dot(x0))
    k = 0
    lamk = num/denom
    
    while k<40:
        denom = num
        evec = Akx0.copy() #take a copy
        Akx0 = (A*Akx0)
        num = (Akx0.dot(x0))
        k += 1
        lamk2 = num / denom
        if abs(lamk - lamk2) < epsilon:
            evec *= (1/abs(evec)) #normalize
            return lamk2,evec,k
        lamk = lamk2

def Randomwalk(seed,steps,start = [0,0]):

    random = randgen(seed)
    points = [[start[0]],[start[1]]]
    for i in range(steps):
        points[0].append(points[i][0] + (2 * random.gen()) - 1)
        points[1].append(points[i][1] + (2 * random.gen()) - 1)
    
    return points

def integrate_montecarlo(f,a,b,N,seed1 = 0):
    rand = randgen(seed = seed1,interval = (a,b))
    sum = 0
    for i in range(N):
        sum += f(rand.gen())
    return sum*((b-a)/N)

def diff_eulerforward(dydx,x0,y0,x1,dx):
    datX = [x0]
    datY = [y0]
    while x0 < x1:
        y0 = y0 + dx*(dydx(y0,x0))
        x0 += dx
        datX.append(x0)
        datY.append(y0)
    return datX, datY

def diff_predictorcorrector(dydx,x0,y0,x1,dx):
    datX = [x0]
    datY = [y0]
    while x0 < x1:
        k1 = dx*dydx(y0, x0)
        k2 = dx*dydx(y0 + k1, x0 + dx)
        y0 = y0 + (k1+k2)/2
        x0 = x0 + dx
        datX.append(x0)
        datY.append(y0)
    return datX, datY

def diff_RK4(dydx,x0,y0,x1,dx):
    datX = [x0]
    datY = [y0]
    while x0 < x1:
        k1 = dx * dydx(y0,x0)
        k2 = dx * dydx((y0 + (k1/2)),(x0 + (dx/2)))
        k3 = dx * dydx((y0 + (k2/2)),(x0 + (dx/2)))
        k4 = dx * dydx((y0 + k3),(x0 + dx))
        y0 = y0 + ((k1 + k4 + (2*(k2 + k3)))/6)
        x0 += dx
        datX.append(x0)
        datY.append(y0)
    return datX, datY

def partialdiff_heatdiffusion(f0,xi,xf,ti,tf,nx,nt,times = []):
    hx = (xf-xi)/nx
    ht = (tf-ti)/nt
    alpha = ht/(hx**2)
    V0 = [f0(xi)]
    X = [xi]
    x = xi + hx
    for i in range(nx):
        X.append(x)
        V0.append(f0(x))
        x += hx
    Vlist = [V0[:]]
    for i in range(1,nt+1):
        V1 = [(alpha*V0[1] + ((1-(2*alpha))*V0[0]))]
        for j in range(1,nx):
            V1.append((alpha*(V0[j+1]+V0[j-1]) + ((1-(2*alpha))*V0[j])))
        V1.append(alpha*V0[nx-1] + ((1-(2*alpha))*V0[nx]))
        V0 = V1[:]
        if i in times:
            Vlist.append(V0[:])
    return X,Vlist

def inv_LU(A):

    n = len(A)

    identitys = [0 for i in range(n)]
    for j in range(n):
         identitys[i] = [[0] for k in range(n)]
         identitys[i][i][0] = 1

    invmat = [[] for l in range(n)]
    for i in range(n):
        tempA = mat_copy(A) #take a copy
        inv = LU_solve(tempA, identitys[i]) 
        for j in range(n):
            invmat[j].append(inv[j][0])
    
    return invmat

def mat_copy(A):
    newA = []
    for i in range(len(A)):
        newA.append(A[i][:])
    return newA


def partition(N,dt,t1,seed):

    N0 = N
    data = [N,0]
    Ns = data[:]

    for i in range(len(data)):
        data[i] = [data[i]]
    
    ran = randgen(seed)
    t = dt
    ts = [0]

    while t <= t1:
        curr = Ns[0]
        prob = curr/N0
        if ran.gen() < prob:
            Ns[0] -= 1
            Ns[1] += 1
        else:
            Ns[0] += 1
            Ns[1] -= 1
        ts.append(t)
        for i in range(len(data)):
            data[i].append(Ns[i])
        t += dt
    return ts,data

    