#program to calculate sum of first N odd numbers and N factorial

n = 5


def sum_odd(n):
    #returns sum of n odd numbers
    sum = 0
    for i in range(1,2 * n,2):
        sum += i
    return sum

def fact(n):
    #returns n factorial
    factorial = 1
    for i in range(n,1,-1):
        factorial = factorial * i
    return factorial

print('Sum of',n,'odd numbers is',sum_odd(n))
print(n,'factorial is',fact(n))
