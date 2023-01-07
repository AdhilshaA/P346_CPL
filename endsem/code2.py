import mylibrary as lib
import matplotlib.pyplot as plt

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('endsem/input2.txt'))  #getting those variables into this code

#using function to simulate the said problem
ts,result = lib.wallhole(Nleft,step,tf,seed1)

#solutions and plotting
plt.plot(ts,result[0],'r-',label = "N(left)",ms = 4)
plt.plot(ts,result[1],'b-',label = "N(right)",ms = 4)
plt.legend()
plt.show()
print("The output is shown in <output2.png>")

######-----  OUTPUT  -----######
'''
The output is attached as <output2.png>
'''