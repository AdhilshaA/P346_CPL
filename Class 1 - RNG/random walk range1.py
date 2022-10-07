import mylibrary as lib
import matplotlib.pyplot as plt

def Randomwalk2D_sim2(seed,steps,start = (0,0)):
    #simulates Random walk, return list of coordinates and prints a Random walk plot with range (root2).
    
    Random_numbers = lib.LCG(seed,steps * 2) #need two coordinates
    points = [start] #list of coordinates visited, stored as tuples
    for i in range(steps):
        # x = points[i][0] + (2 * Random_numbers[i]) - 1
        # y = points[i][1] + (2 * Random_numbers[(steps + i)]) - 1
        if (2 * Random_numbers[i]) - 1 < 0:
            x = points[i][0] - 1
        else:
            x = points[i][0] + 1
        if (2 * Random_numbers[steps + i]) - 1 < 0:
            y = points[i][1] - 1
        else:
            y = points[i][1] + 1
        points.append((x,y))
    
    #graph formatting
    plt.title('Random walk with {} steps'.format(steps))
    plt.axhline(0,lw = 1,c = 'k')
    plt.axvline(0,lw = 1,c = 'k') 
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.plot([start[0]],[start[1]],'go',ms = 4) #plotting thte start point as green
    plt.plot([points[i][0] for i in range(steps+1)],[points[i][1] for i in range(steps+1)],'-bo',lw = '1',ms = 1, mec = 'k', mfc = 'b' )
    plt.plot([points[-1][0]],[points[-1][1]],'ro',ms = 3) #plotting the end point as red
    plt.show()
    #points[i][0] is the (i)th x cordinate and points[i][1] is the (i)th y cordinate, then a list of each
    return points


R1 = Randomwalk2D_sim2(23,300)
print('rms =',lib.rms_walk(R1),',netd =',lib.netdisplace_walk(R1))