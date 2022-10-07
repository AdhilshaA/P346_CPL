import mylibrary as lib
import matplotlib.pyplot as plt
from math import log2
numbers = [23,27,3,7,8,9,11]
m = 10000000
r = lib.randgen(21)
# for i in numbers: #for certain sets of numbers
#     number = i

for i in range(1,1000001): #for all numbers in certain range
    number = i

# for i in range(100000):   #for random numbers in range
#     number = ((r.gen() * m) // 1)
#     while number == 0:
#         number = ((r.gen() * m) // 1)
    # print('taking number',number)
    l = [number]
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            newnumber = (3 * number) + 1
            power = log2(newnumber)
            if power % 2 == 1:
                print('GOtcha! the number is',number)
            number = newnumber
        l.insert(0,number)
    plt.plot(l,marker = 'o',ms = 4)
    

plt.show()