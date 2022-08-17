# calulate pi over 2000 trials

#LCG function
def LCG(m,c,a,seed,length):

    RNs = [seed / m]

    for i in range(1,length):
        RNs.append(((((a * RNs[i-1])+c) % m) / m))
    return RNs

inside = 0

#all variables
length = 2000
m = 32768
c = 12345
a = 1103515245
seed1 = 20
seed2 = 21


xlist = LCG(m,c,a,seed1,length)
ylist = LCG(m,c,a,seed2,length)


for i in range(length):
    if ( ((xlist[i]) ** (2)) + ((ylist[i]) ** (2)) ) <= 1:
        inside += 1

pi_val = 4 * (inside / length)

print(pi_val)
