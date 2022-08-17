start = 10
cd = 1.5
cr = 0.5
n = 5

def sum_ap(start,cd,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an AP specified by first term and common difference
    for i in range(n):
        sum += term
        term += cd
    return sum

def sum_hp(start,cd,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an HP specified by first term and common difference of its corresponding AP
    for i in range(n):
        sum += 1 / term
        term += cd
    return sum

def sum_gp(start,cr,n):
    sum = 0
    term = start
    #returns the sum of first n terms in an GP specified by first term and common ratio
    for i in range(n):
        sum += term
        term = term * cr
    return sum


print('For first term = ',start,', common difference = ',cd,', and common ratio ',sep ='')

print('ap',sum_ap(start,cd,n))
print('gp',sum_gp(start,cr,n))
print('hp {:.4f}'.format(sum_hp(start,cd,n)))