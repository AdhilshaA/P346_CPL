#program to calculate sum of first N odd numbers and N factorial

#variables
n1 = 5  #no. of terms of sumof term
n2 = 3  #the n whose factorial is calculated

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

print('Sum of',n1,'odd numbers is',sum_odd(n1))
print(n2,'factorial is',fact(n2))

#  OUTPUT
'''
Sum of 5 odd numbers is 25
3 factorial is 6
'''
