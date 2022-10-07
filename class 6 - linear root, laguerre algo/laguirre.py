import mylibrary as lib
import math as m

def deflate_px(px, root):

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



def derivative_px(px):
    n = len(px) - 1
    i = 0
    while n != 0:
        px[i] = px[i] * (n)
        i += 1
        n -= 1
    return px[:-1]

def value_px(px,x):
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
        if abs(value_px(px,guess)) < tolerance:
            print('{}th root {} found in 0 steps.'.format(steps,guess))
            steps += 1
            roots.append(guess)
            px = deflate_px(px,guess)
            n -= 1
            continue
        # print('Finding the {}th root for {}'.format(steps,px))
        dpx = derivative_px(px[:])
        ddpx = derivative_px(dpx[:])
        i = 1
        theguess = guess
        while True:
            g = value_px(dpx,theguess)/value_px(px,theguess)
            h = (g**2) - (value_px(ddpx,theguess)/value_px(px,theguess))
            if g < 0:
                a = (n / (g - m.sqrt((n-1)*((n*h)-(g**2)))))
            else:
                a = (n / (g + m.sqrt((n-1)*((n*h)-(g**2)))))
            # print('a is',a)
            newguess = theguess - a
            # print(value_px(px,theguess),'and',value_px(px, newguess))
            
            if i < 26 :
                # if abs(a) < tolerance and value_px(px,newguess) < tolerance:
                if value_px(px,newguess) < tolerance:
                    print('{}th root is {} found in {} steps.'.format(steps,newguess,i))
                    steps += 1
                    roots.append(newguess)
                    px = deflate_px(px,newguess)
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
    