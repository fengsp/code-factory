#!/usr/bin/env python
# -*- coding: UTF-8 -*-
x = 2
S = [1, 2, 3, 4, 5, 6, 7]
assert x*sum(S) == sum(x*y for y in S)

def Su(seq, i=0):
    if i == len(seq): return 0;
    return Su(seq, i+1) + seq[i]
assert Su(S) == 28

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

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

seq = [1, 2, 5, 7, 8, 3]
seq2 = seq[:]
gnomesort(seq)
print seq
print mergesort(seq2)
