#To find the sum of a certain series accurate upto 4 place in decimals an plot sum versus n (number of terms)

n = 30

term = -1
series_terms = []
sum = 0
for i in range(n):
    term = term * ((-1) / 2)
    series_terms.append(term)
    sum += term

#use gp (too many fn. calls) or write sep. function

import matplotlib.pyplot as plt

plt.plot(series_terms)
plt.show()