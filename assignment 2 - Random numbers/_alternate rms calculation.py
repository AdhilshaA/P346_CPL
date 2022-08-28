# A follow up code from my query through mail to Sir.
# RMS distance calculation redefined under average assumption.

import mylibrary as lib
from math import sqrt


def rms_walk2(walk):
    #calculating rms distance from a 2D walk

    steps = len(walk) - 1  #n steps = n + 1 coordinates
    sumof_dsquared = 0
    for i in range(1,steps):
        sumof_dsquared += (((walk[i][0] - walk[i-1][0]) ** 2) + ((walk[i][1] - walk[i-1][1]) ** 2))
        # eqn.                  (  x2   -   x1  ) ^ 2         +      (  y2   -   y1  ) ^ 2 
    
    # rms = sqrt(sumof_dsquared / steps)  # NOT taking average, assuming that each step in this simulation is the average of Random walk done multiple times
    rms = sqrt(sumof_dsquared)

    return rms

R1 = lib.Randomwalk2D_sim(16,600) #returns coordinates
print('For a walk of {} steps, rms steps as per old calculations is {:.4f} and rms distance as per new calculation is {:.4f}\n the net dispaceament is netd = {:.4f}'.format(600,lib.rms_walk(R1),rms_walk2(R1),lib.netdisplace_walk(R1)))
R2 = lib.Randomwalk2D_sim(25,900)
print('For a walk of {} steps, rms steps as per old calculations is {:.4f} and rms distance as per new calculation is {:.4f}\n the net dispaceament is netd = {:.4f}'.format(900,lib.rms_walk(R2),rms_walk2(R2),lib.netdisplace_walk(R2)))

# OUTPUT
'''
For a walk of 600 steps, rms steps as per old calculations is 0.8182 and rms distance as per new calculation is 20.0411
 the net dispaceament is netd = 13.2422
For a walk of 900 steps, rms steps as per old calculations is 0.8108 and rms distance as per new calculation is 24.3242
 the net dispaceament is netd = 18.8460
 '''
 # In this case, the rms distance is ~ ( <r>.rootN ) where <r> is the average step ~ 0.8 as per earlier simulations.
 # Here, the net displacement and rms distance is also comparable for larger N values


####-----------------  DETAILS OF DISCUSSION FOR REFERENCE  ----------------#####

# In our question, we are simulating only 3 Random walks (one each for 300, 600, and 900 steps). As per the discussions we had about RMS distance in class, We find rms distance by taking the distances covered in each step, taking its square, finding its mean, and then taking root.    But that would only give you the RMS distance it traveled in one step. Comparing it with net displacement is not possible. (example of a Random walk simulated with seed = 16 and 600 steps has RMS distance = 0.8182 units and net displacement = 13.2422 )
#
# In searching about RMS distance in Random walk, I found that,
# First, they simulate the Random walk of N steps multiple times. Then they find the average of the square of step distances. Then, add them and take its root. (equivalent to RMS of net distance traveled), This term is proportional to rootN for steps of fixed length and hence can be compared to net displacement.
#
# <d2> = <(a1 + a2 + a3 + ... + aN)2> = <(a1 + a2 + a3 + ... + aN) (a1 + a2 + a3 + ... + aN)>
#
#          = (<a12> + <a22> + <a32> + ... + <aN2>) + 2 (<a1a2> + <a1a3> + ... <a1aN> + <a2a3> + ... <a2aN> + ...)
#
#          = (1 + 1 + 1 + ... +1) + 2 (0 + 0 + ... + 0 + 0 + ...) = N
# sqrt(<d2>)=sqrt(N)
#
# Here d is the net distance, ai is the ith step and <> notates 'average over many experiments' (Here, the step distance is set to 1 hence 1.rootN)
#
# possible solution would be to NOT find the mean of d squares. Adding them together and taking root will be equivalent to process (assuming that our simulation is an equivalent of the average of multiple simulations of the same steps, which is not the case and wont get accurate value). The alternative is to redefine rms calculation by simulating same walk multiple times.
#
# (I haven't considered here the variable step length of the simulation we are doing in the calculation which, in the correct method, gives something like (<r>rootN) where <r> average step distance, in our case might be ~0.8 as per my simulations)