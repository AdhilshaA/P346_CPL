import mylibrary as lib
import math as m
import matplotlib.pyplot as plt

vals=[142,109,130,111,103,152,131,117,155,135,111,151,121,102,143,147,125,156,137,125,155,152,134,149,109,141,106,143,128,152,147,154,106,159,142,141,110,152,149,123,112,128,112,155,156,128,142,140,158,140,132,123,116,158,153,137,116,127,144,110,145,146,155,118,113,129,106,159,112,120,155,120,116,145,159,106,150,146,139,139,139,102,154,137,127,134,135,126,138,123,117,151,112,103,153,132,144,156,154,132]

# print("vals",vals)
# print("lenvals",len(vals))
# for bin in range(15,31):
#     plt.hist(vals, bins = bin, rwidth = 0.9, color = 'blue', align = 'mid')
#     plt.title("Beta source counts histogram")
#     plt.ylabel("no. of times")
#     plt.xlabel("counts - 25 sec")
#     plt.savefig(f"images/{bin}.png")
#     plt.show()


vals=[1037,1025,1041,961,1030,1084,964,1038,1039,1065,1063,1015,1084,1040,1001,1041,993,1026,974,1094,1046,1059,1020,1050,1006,1035,1061,1072,1028,984,1028,1020,1088,994,1047,1031,1076,970,1011,1058,1040,1011,1026,1027,1095,1048,1036,998,1021,1061]
print("vals",vals)
print("lenvals",len(vals))
plt.hist(vals, bins = 15, rwidth = 0.9, color = 'blue', align = 'mid')
plt.title("Beta source counts histogram")
plt.ylabel("no. of times")
plt.xlabel("counts - 25 sec")
plt.show()