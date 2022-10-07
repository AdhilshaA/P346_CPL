import mylibrary as lib
import matplotlib.pyplot as plt

m = 1000
r = lib.randgen(21)
for i in range(30):
    number = (r.gen() * m) // 1
    print(list(number))
#     l = list(number)
#     while number != 1:
#         if number % 2 == 0:
#             number = number / 2
#         else:
#             number = (3 * number) + 1
#         l.insert(0,number)
#     plt.plot(l)
    

# plt.show()