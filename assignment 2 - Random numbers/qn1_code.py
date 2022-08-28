#LCG random generator code

#code in myLibrary.
#HEre, Sample call and output as graph

import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. 
locals().update(lib.parse('assignment 2 - Random numbers/qn1_input.txt'))  #getting those variables into this code

###--  variables and meaning  --###
# seed - seed for LCG random generator
# length - no. of random numbers needed
# Random_Numbers - list of random numbers

Random_Numbers = lib.LCG(seed, length)   #default a,c,m value and range 0 to 1
plt.plot(Random_Numbers,'o',markersize = 4)
plt.title('Scatter plot for LCG with seed {}'.format(seed))
plt.xlabel('Index')
plt.ylabel('Random Number')
plt.yticks([i*0.04 for i in range(25)])
plt.show()


######-----  OUTPUT  -----######
'''
<Graph attached as 'qn1_output sample LCG graph.png'>
'''
