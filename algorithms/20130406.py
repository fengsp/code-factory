x = 100
def test1(S):
    return x*sum(S) == sum(x*y for y in S)
assert test1([10, 10])


from random import randrange
n = 10**90
p = randrange(n)
from math import log
# print log(n, 2)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True
assert is_prime(5)


# Gnome Sort
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1


# Merge Sort
def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res
testseq = [randrange(200) for i in range(100)]
from pprint import pprint
# pprint(mergesort(testseq))


# reduction
dd = float("inf")
for x in testseq:
    for y in testseq:
        if x == y: continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
sortedseq = sorted(testseq)
for i in range(len(sortedseq)-1):
    x , y = sortedseq[i], sortedseq[i+1]
    if x == y: continue
    d = abs(x-y)
    if d < dd:
        xx, yy, dd = x, y, d
print("xx and yy is: " + str(xx) + " " + str(yy))





