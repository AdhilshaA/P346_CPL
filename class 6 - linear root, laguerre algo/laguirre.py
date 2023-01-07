import mylibrary as lib
import math as m

def px_deflate(px, root):

    #Here, the passed 'root' is a verified root from main body with a certain tolerance, therefore checking not done.
    if len(px) == 1:
        print('P(x) doesnt contain any x: deflation exited!')
        return None
    if px[0] != 1:
        lead = px[0]
        for i in range(len(px)):
            px[i] = px[i] / lead
    for i in range(1,len(px)):
        px[i] = (px[i-1] * root) + px[i]
    return px[:-1]

def px_derivative(px):
    n = len(px) - 1
    i = 0
    while n != 0:
        px[i] = px[i] * (n)
        i += 1
        n -= 1
    return px[:-1]

def px_value(px,x):
    print('finding',px)
    sum = 0
    i = 0
    n = len(px) - 1
    while n >= 0:
        sum+= (px[i] * (x**n))
        i += 1
        n -= 1
    return sum

def root_laguire(px,guess,tolerance):
    roots = []
    steps = 1
    N = len(px) - 1
    n = N
    while steps <= N:
        if abs(px_value(px,guess)) < tolerance:
            print('{}th root {} found in 0 steps.'.format(steps,guess))
            steps += 1
            roots.append(guess)
            px = px_deflate(px,guess)
            n -= 1
            continue
        # print('Finding the {}th root for {}'.format(steps,px))
        dpx = px_derivative(px[:])
        ddpx = px_derivative(dpx[:])
        i = 1
        theguess = guess
        while True:
            g = px_value(dpx,theguess)/px_value(px,theguess)
            h = (g**2) - (px_value(ddpx,theguess)/px_value(px,theguess))
            if g < 0:
                a = (n / (g - m.sqrt((n-1)*((n*h)-(g**2)))))
            else:
                a = (n / (g + m.sqrt((n-1)*((n*h)-(g**2)))))
            # print('a is',a)
            newguess = theguess - a
            # print(px_value(px,theguess),'and',px_value(px, newguess))
            
            if i < 26 :
                # if abs(a) < tolerance and px_value(px,newguess) < tolerance:
                if px_value(px,newguess) < tolerance:
                    print('{}th root is {} found in {} steps.'.format(steps,newguess,i))
                    steps += 1
                    roots.append(newguess)
                    px = px_deflate(px,newguess)
                    n -= 1
                    break
                # else:
                #     print('Guess discarded.\n')

            else:
                print('The guess for {} th root was not found in 25 steps'.format(steps))
                return None
            theguess = newguess
            i += 1
    return roots
            
        


tolerance = 0.0001
px = [1,-1,-7,1,6]


guesss = 0
print(root_laguire(px,guesss,tolerance))
    