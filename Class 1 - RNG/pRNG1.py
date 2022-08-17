import matplotlib.pyplot as plt

xaxis=list(i for i in range(1,201))
RNs =[0.1]
c = 3.5
for i in range(1,200):
    RNs.append(RNs[i-1] * c * (1 - RNs[i-1]))

plt.plot(xaxis,RNs)
plt.xlabel('index of random number')
plt.ylabel('Random number')
plt.title('pRNG')
plt.show()
print('')
plt.scatter(xaxis,RNs)
plt.xlabel('index of random number')
plt.ylabel('Random number')
plt.title('pRNG')
plt.show()