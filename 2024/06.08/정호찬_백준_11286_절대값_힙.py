"""
    메모리 : 39960 KB
    시간 : 140 ms 
"""
import sys
from heapq import heappush, heappop 

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)