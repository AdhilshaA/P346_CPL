def lagrange_intrapolate(X,Y,x1):
    N = len(X)
    if N != len(Y):
        print('data mismatch')
        return None
    sum = 0
    for i in range(N):
        prdct = 1
        for k in range(N):
            if k == i:
                continue
            prdct = prdct * ((x1 - X[k])/(X[i]-X[k]))
        sum += prdct * Y[i]
    return sum

X = [2,3,5,8,12]
Y = [10,15,25,40,60]
x1 = 4

print(lagrange_intrapolate(X,Y,x1))
        
X = [0,10,20,30]
Y = [-250,0,50,-100]
x1 = 15

print(lagrange_intrapolate(X,Y,x1))

X = [1951,1961,1971]
Y = [2.8,3.2,4.5]
x1 = 1969

print(lagrange_intrapolate(X,Y,x1))
