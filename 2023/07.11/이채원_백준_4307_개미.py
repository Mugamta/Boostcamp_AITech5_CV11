#문제처음읽고 : 방향을 모른다. 경우의 수 중 최대와 최소 모두 구해야 함 => 완전 탐색?


import sys
from itertools import product

t_n = int(input())#test case의 수 n
for _ in range(t_n) :
    l, n = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n) :
        g = int(input())
        arr.append(g)
    for p in product([-1,1], repeat = n) : #각 개미의 방향 경우의 수 
        #-1이면 왼쪽, 1이면 오른쪽 방향
        time = 0 
        while True : 
            time += 1
            for


    
