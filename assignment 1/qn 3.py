#To find the sum of a certain series accurate upto 4 place in decimals an plot sum versus n (number of terms)

import matplotlib.pyplot as plt

#variables
n = 15

# Given series had terms (second term onwards) of GP with starting term -1 and common ratio (-0.5)
term = -1
stepwise_sum = []
total_sum = 0
for i in range(n):
    term = term * ((-1) / 2) #develops terms (starting from second) as in the mentioned GP
    total_sum += term
    stepwise_sum.append(total_sum)

print('The sum of the given series upto {} terms are {:.4f}'.format(n, total_sum))

plt.axhline(total_sum)
plt.plot(stepwise_sum,'r-o')
plt.yticks([i * 0.04 for i in range(15)])
plt.title('Sum vs N plot')
plt.xlabel('N')
plt.ylabel('Sum')
plt.show()

#  OUTPUT
'''
The sum of the given series upto 15 terms are 0.3333

(The plot is attached as Qn5 sum vs n plot.png in the same folder)
'''