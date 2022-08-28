#Add the next random coord to previous one
#use (random number * 2) - 1 so its range is -1 + 1
# Simulating different Random walks of different length and 

import mylibrary as lib

#parsing the inputs using my own parsing function. Check mylibrary for more details
locals().update(lib.parse('assignment 2 - Random numbers/qn3_input.txt'))  #getting those variables into this code

###--  variables and meaning  --###
# !! 3 variable each for i=1,2,3 !!#
# Seed(i) : seed for first Random walk(i)
# steps(i) : no. of steps in Random walk(i)
# Rwalk(i) : list of coordinates of Random walk(i), each coordinate in tuple.
# rms(i)  : rms distance value of Random walk(i)
# displace(i) : dispacement of Random walk(i)

#simulating Random walks
Rwalk1 = lib.Randomwalk2D_sim(seed1, steps1)
Rwalk2 = lib.Randomwalk2D_sim(seed2, steps2)
Rwalk3 = lib.Randomwalk2D_sim(seed3, steps3)
#generates the graphs too


#calculating rms distances as per algorithm discussed in class
rms1 = lib.rms_walk(Rwalk1)
rms2 = lib.rms_walk(Rwalk2)
rms3 = lib.rms_walk(Rwalk3)

#calculating total displacement of a given walk
displace1 = lib.netdisplace_walk(Rwalk1)
displace2 = lib.netdisplace_walk(Rwalk2)
displace3 = lib.netdisplace_walk(Rwalk3)

print('For origin as starting point, seed = {} and {} steps,\n\t the rms distance  = {:.4f} and the net displacement = {:.4f}\n'.format(seed1,steps1,rms1,displace1))
print('For origin as starting point, seed = {} and {} steps,\n\t the rms distance  = {:.4f} and the net displacement = {:.4f}\n'.format(seed2,steps2,rms2,displace2))
print('For origin as starting point, seed = {} and {} steps,\n\t the rms distance  = {:.4f} and the net displacement = {:.4f}\n'.format(seed3,steps3,rms3,displace3))

######-----  OUTPUT  -----######
'''
<Random walk 1 simulated graph attached as 'qn3_outputRwalk1(300)'>
<Random walk 2 simulated graph attached as 'qn3_outputRwalk2(600)'>
<Random walk 3 simulated graph attached as 'qn3_outputRwalk3(900)'>

For origin as starting point, seed = 21 and 300 steps,
         the rms distance  = 0.8068 and the net displacement = 2.1847

For origin as starting point, seed = 16 and 600 steps,
         the rms distance  = 0.8182 and the net displacement = 13.2422

For origin as starting point, seed = 29 and 900 steps,
         the rms distance  = 0.8267 and the net displacement = 26.2499

'''
# The rms distance in this case is actually rms step distance which, in no way, is comparable to the net dispacement.
# See alternate calculation for more details