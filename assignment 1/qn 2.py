#sum of n terms of N terms in AP, HP, and GP

#variables
start = 10   #first term
n = 5        #no. of terms


#given
cd = 1.5     #common difference
cr = 0.5     #common ratio

def sum_ap(start,cd,n):
    #returns the sum of first n terms in an AP specified by first term and common difference
    sum = 0
    term = start
    for i in range(n):
        sum += term
        term += cd
    return sum

def sum_hp(start,cd,n):
    #returns the sum of first n terms in an HP specified by first term and common difference of its corresponding AP
    sum = 0
    term = start
    for i in range(n):
        sum += 1 / term
        term += cd
    return sum

def sum_gp(start,cr,n):
    #returns the sum of first n terms in an GP specified by first term and common ratio
    sum = 0
    term = start
    for i in range(n):
        sum += term
        term = term * cr
    return sum


print('For the first term ',start,', common difference ',cd,', common ratio ',cr,' and number of terms ',n,',',sep ='')
print('AP sum: {:.4f}'.format(sum_ap(start,cd,n)))
print('GP sum: {:.4f}'.format(sum_gp(start,cr,n)))
print('HP sum: {:.4f}'.format(sum_hp(start,cd,n)))

#  OUTPUT
'''
For first term 10, common difference 1.5, common ratio 0.5 and number of terms 5,
AP sum: 65.0000
GP sum: 19.3750
HP sum: 0.3953
'''