# Writing LCG



def LCG(seed, length, a = 1103515245, c = 12345 ,m = 32768):
    # function for LCG that generates random numbers in range (0,1)
    #default a, c, m value set. can change in case specified
    RNs = [seed / m]

    for i in range(1,length):
        RNs.append(((((a * RNs[i-1])+c) % m) / m))
    return RNs

#variables
m = 32768
c = 12345
a = 1103515245
seed = 10
length = 200


RNs =LCG(m,c,a,seed,length)

#index axis values
xaxis = [i for i in range(1,201)]

# plotting randomnumbers in normal and scatter plot
import matplotlib.pyplot as plt

plt.plot(xaxis,RNs)
plt.xlabel('index of random number')
plt.ylabel('Random number')
plt.title('pRNG')
plt.show()

plt.scatter(xaxis,RNs)
plt.xlabel('index of random number')
plt.ylabel('Random number')
plt.title('pRNG')
plt.show()
