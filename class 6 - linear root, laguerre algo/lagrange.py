x = [2,3,5,8,12]
y = [10,15,25,40,60]

x1 = 4

def lagrange_intrapolate(x,y,x1):
    N = len(x)
    if N != len(y):
        print('data mismatch')
        return None
    sum = 0
    for i in range(N):
        prdct = 1
        for k in range(N):
            if k == i:
                continue
            prdct = prdct * ((x1 - x[k])/(x[i]-x[k]))
        sum += prdct * y[i]
    return sum

x = [2,3,5,8,12]
y = [10,15,25,40,60]
x1 = 4

print(lagrange_intrapolate(x,y,x1))
        
x = [0,10,20,30]
y = [-250,0,50,-100]
x1 = 15

print(lagrange_intrapolate(x,y,x1))

x = [1951,1961,1971]
y = [2.8,3.2,4.5]
x1 = 1969

print(lagrange_intrapolate(x,y,x1))
