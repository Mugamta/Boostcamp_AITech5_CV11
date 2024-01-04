import sys
from collections import deque


cost = int(sys.stdin.readline())
N = int(sys.stdin.readline()) 
arr = list(list(map(int, sys.stdin.readline().split())))
temp = cost
dd = dict()
for s, e, c in arr :
    if s not in dd :
        dd[s] = [e,c]
    else : 
        _, old_cost = dd[s]
        dd[s] = e, old_cost + c
        

