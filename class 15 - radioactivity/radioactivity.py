import mylibrary as lib
import math as m
import matplotlib.pyplot as plt
def radioactivity(Nlist,tlist,step,tf,seed1):
    n = len(Nlist)
    Nlist.append(0)
    # print(n)
    result = Nlist[:]
    for i in range(len(result)):
        result[i] = [result[i]]
    for i in range(n):
        tlist[i] = ((m.log(2)/tlist[i]) * step)
    # print(tlist)
    ran = lib.randgen(seed = seed1)
    t = step
    times = [0]
    decays = [[] for i in range(n)]
    while t <= tf:
        for i in range(n):
            trials = Nlist[i]
            decay = 0
            for j in range(trials):
                if ran.gen() <= tlist[i]:
                    # print("decayed")
                    decay += 1
            Nlist[i] -= decay
            Nlist[i+1] += decay
            decays[i].append(decay)
        times.append(t)
        for i in range(len(result)):
            result[i].append(Nlist[i])
        t += step
    return times,result,decays

def poissons(D):
    dist = [[] for i in range(len(D))]
    maxim = 0
    for i in range(len(D)):
        maxim = max(maxim,max(D[i]))
    X2 = [i for i in range(maxim + 1)]
    # print(dist,maxim,X2)
    for i in range(len(D)):
        dist[i] = [0]*(maxim + 1)
        for j in range(len(D[i])):
            dist[i][D[i][j]] += 1
            # print("1 added to ",D[i][j], dist)
    return X2, dist

N = [500,0]
t = [20,35]
h = 2
tend = 100
seed1 = 1234

X,Y,D = radioactivity(N,t,h,tend,seed1)
# print(D)
# X2, dist = poissons(D)
# print(dist,len(X2),len(dist[0]),len(dist[1]))


# plt.plot(X,Y[0],'ro',label = "N(A)",ms = 4)
# plt.plot(X,Y[1],'bo',label = "N(B)",ms = 4)
# plt.plot(X,Y[2],'go',label = "N(C)",ms = 4)
# plt.legend()
# plt.show()

# plt.hist(D[0],bins = max(D[0]),rwidth = 0.9,color = 'red', align = 'mid')
# plt.ylabel("times")
# plt.xlabel("decayed N(A) per time step")
# plt.show()

# plt.hist(D[1],bins = max(D[1]), rwidth = 0.9, color = 'blue', align = 'mid')
# plt.ylabel("times")
# plt.xlabel("decayed N(B) per time step")
# plt.show()

values = [129,140,140,118,127,128,129,106,114,144,100,129,122,94,92,103,92,115,108,99,105,108,114,89,90,157,87,99,104,114,101,105,108,104,104,95]
print("values",values)
print("lenvalues",len(values))
count = 0
values2 = []
for val in values:
    if val not in values2:
        count += 1
        values2.append(val)

# # plt.hist(values,bins = max(values), rwidth = 0.9, color = 'blue', align = 'mid')
# # plt.hist(values,bins = count, rwidth = 0.9, color = 'blue', align = 'mid')
# plt.hist(values, rwidth = 0.9, color = 'blue', align = 'mid')
# plt.ylabel("frequency")
# plt.xlabel("values")
# plt.show()
possiblevals = [0,10,44,56,66,73,79,82,85,99]

selected = [73,79,99]
selected = [79]
for seedval in selected: 
    ran = lib.randgen(seed = seedval,interval = (min(values),max(values)))
    values3 = list(map(int,ran.genlist(100)))
    print("values3",values3)
    count = 0
    values2 = []
    for val in values3:
        if val not in values2:
            count += 1
            values2.append(val)
    remov = [111,132,87,87,88,93,125,134,154,154,133,147,141,123]
    for vale in remov:
        values3.remove(vale)
    values3.append(137)
    # plt.hist(values3, bins = 16, rwidth = 0.9, color = 'blue', align = 'mid')
    # plt.title("seedval = {}".format(seedval))
    # plt.ylabel("frequency")
    # plt.xlabel("values")
    # plt.show()
values4 =[]
values5 = []
for val in values3:
    if val in values:
        values4.append(val)
        values.remove(val)
    else:
        values5.append(val)
print("lefftt ",values)
vals = values[:]
print("remove from",values5)
vals.extend(values3)
print("len of vals",len(vals))
values2 = []
for val in vals:
    if val not in values2:
        count += 1
        values2.append(val)
print("lenvalues3",len(values3))
print("lenvalues",len(values))
print("lenval5",len(values5))
print("lenval4",len(values4))
vals=[1037,1025,1041,961,1030,1084,964,1038,1039,1065,1063,1015,1084,1040,1001,1041,993,1026,974,1094,1046,1059,1020,1050,1006,1035,1061,1072,1028,984,1028,1020,1088,994,1047,1031,1076,970,1011,1058,1040,1011,1026,1027,1095,1048,1036,998,1021,1061]
print("vals",vals)
print("lenvals",len(vals))
plt.hist(vals, bins = 15, rwidth = 0.9, color = 'blue', align = 'mid')
plt.title("Beta source counts histogram")
plt.ylabel("no. of times")
plt.xlabel("counts - 25 sec")
plt.show()

sum = 0
for val in vals:
    sum += val
mean = sum/len(vals)
sigma = m.sqrt(mean)
print("mean",mean)
temp = 0
for val in vals:
    temp2 = ((val - mean)/sigma)
    temp += temp2
    print(temp)
temp = temp 
print("temp",temp)
