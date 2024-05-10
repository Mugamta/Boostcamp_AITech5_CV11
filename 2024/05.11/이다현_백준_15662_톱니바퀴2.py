import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
maps=[deque(map(int, input().strip())) for _ in range(T)]

def move(n,d):
    global c_r, c_l, maps
    ori_d=d

    for i in reversed(range(n)): # 왼쪽
        if maps[i][2]!=c_l:
            c_l=maps[i][6]
            maps[i].rotate(d*-1)
            d*=-1
        else:
            break
    d=ori_d
    for i in range(n+1,T): # 오른쪽
        if maps[i][6]!=c_r:
            c_r=maps[i][2]
            maps[i].rotate(d*-1)
            d*=-1
        else:
            break

K=int(input())
for _ in range(K):
    n,d=map(int, input().split())
    c_l,c_r=maps[n-1][6],maps[n-1][2]
    maps[n-1].rotate(d)
    move(n-1,d)
print(sum([1 if w[0] == 1 else 0 for w in maps]))
