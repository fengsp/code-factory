# StarAdventure
from pprint import pprint
from copy import deepcopy
maxlist = []
N = 10
# building of starblock
# 303
starblockcpp5 = [
    "0123456789", "0123456789", "0123456789", "0123456789", "0123456789", "0123456789", "0123456789", "0123456789", "0123456789", "0123456789"]
starblockcpp3 = [
    "01",
    "11"]
starblockcpp4 = [
    "0123456789", "1234567899", "2345678999", "3456789999", "4567899999", "5678999999", "6789999999", "7899999999", "8999999999", "9999999999"]
# 335
starblockcpp = [
    "0123456789", "1123456789", "2223456789", "3333456789", "4444456789", "5555556789", "6666666789", "7777777789", "8888888889", "9999999999"]
# 450
starblockcpp2 = [
    "0999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"
    ,"9999999999"]

starblock = []
for i in range(N):
    starblock.append([])
    for j in range(N):
        starblock[i].append(int(starblockcpp5[i][j]))
pprint(starblock)

# one simple add function
def add(x, y):
    return x+y

# calculate the maxvalue of the up thing
def maxvalue(n, i, j, k):
    maxvaluelist = []
    if i > 0:
        maxvaluelist.append(maxlist[i-1][j][k] + starblock[n][i])
        if j > i+1:
            maxvaluelist.append(maxlist[i-1][j-1][k] + starblock[n][j] + starblock[n][i])
            if k > j+1:
                maxvaluelist.append(maxlist[i-1][j-1][k-1] + starblock[n][i] + starblock[n][j] + starblock[n][k])
        if k > j+1:
            maxvaluelist.append(maxlist[i-1][j][k-1] + starblock[n][i] + starblock[n][k])
    if j > i+1:
        maxvaluelist.append(maxlist[i][j-1][k] + starblock[n][j])
        if k > j+1:
            maxvaluelist.append(maxlist[i][j-1][k-1] + starblock[n][j] + starblock[n][k])
    if k > j+1:    
        maxvaluelist.append(maxlist[i][j][k-1] + starblock[n][k])
    maxvaluelist.append(maxlist[i][j][k] + starblock[n][i] + \
                        starblock[n][j] + starblock[n][k])
    return max(maxvaluelist)

# initialize our maxlist
for i in range(N):
    maxlist.append([])
    for j in range(N):
        maxlist[i].append([])
        for k in range(N):
            maxlist[i][j].append(reduce(add, [starblock[0][index] for index in range(0, k+1)]))
# pprint(maxlist)

# Here is our algorithm
for n in range(1, N):
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                maxlist[i][j][k] = maxlist[i][j][k] + starblock[n][i] + starblock[n][j] + \
                                   starblock[n][k]
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (i > 0):
                    maxlist[i][j][k] = max(maxlist[i][j][k], maxlist[i-1][j][k] + starblock[n][i])
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (j > i+1):
                    maxlist[i][j][k] = max(maxlist[i][j][k], maxlist[i][j-1][k] + starblock[n][j])
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (k > j+1):
                    maxlist[i][j][k] = max(maxlist[i][j][k], maxlist[i][j][k-1] + starblock[n][k])
"""
maxnumlist = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            maxlist[i][j][k] += reduce(add, [starblock[9][index] for index \
            in range(i, N)], 0)
            maxnumlist.append(maxlist[i][j][k])
            """
# pprint(maxnumlist)
#maxnum = max(maxnumlist)
print maxlist[7][8][9]

