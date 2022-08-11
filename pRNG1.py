import matplotlib.pyplot as plt

x-axis=list(i for i in range(1,201))
RNs =[0.1]
seed = 0.1
c = 3.5
for i in range(1,201):
    RNs[i] = RNs[i-1] * c * (1 - RNs[i-1])

plt.plot(x-axis,RNs)

plt.xlabel('index of random number')
plt.ylabel('Random number')

plt.title('pRNG')

plt.show()
