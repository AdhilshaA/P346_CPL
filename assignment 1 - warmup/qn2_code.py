#sum of n terms of N terms in AP, HP, and GP

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details.
locals().update(lib.parse('assignment 1 - warmup/qn2_input.txt'))  #getting those variables into this code


print('For the first term ',start,', common difference ',cd,', common ratio ',cr,' and number of terms ',n,',',sep ='')
print('AP sum: {:.4f}'.format(lib.sum_ap(start,cd,n)))
print('GP sum: {:.4f}'.format(lib.sum_gp(start,cr,n)))
print('HP sum: {:.4f}'.format(lib.sum_hp(start,cd,n)))

#  OUTPUT
'''
For first term 10, common difference 1.5, common ratio 0.5 and number of terms 5,
AP sum: 65.0000
GP sum: 19.3750
HP sum: 0.3953
'''