def sum_ap(start,cd,n):
    sum = 0
    #returns the sum of first n terms in an AP specified by first term and common difference
    for i in range(start,start + (n * cd), cd):
        sum += i
    return sum

def sum_hp(start,cd,n):
    sum = 0
    #returns the sum of first n terms in an HP specified by first term and common difference of its corresponding AP
    for i in range(start,start + (n * cd), cd):
        sum += 1 / i
    return sum