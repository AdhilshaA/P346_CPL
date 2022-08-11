RNs =[0.1]
seed = 0.1
c = 3.5
for i in range(1,201):
    RNs[i] = RNs[i-1] * c * (1 - RNs[i-1])

