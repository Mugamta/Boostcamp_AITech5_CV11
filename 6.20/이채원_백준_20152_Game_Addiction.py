#맨처음 봤을때는 BFS생각이 남 (최단경로, 가중치없음)
#풀다보니 DP

import sys


def game() :
    H, N = map(int, sys.stdin.readline().split()) #집(H,H)과 PC방(W,W) 좌표 
    L = max(H, N) - min(H, N) 
    if L == 0 : 
        return 1

    arr = list(list(0 for _ in range(L+1)) for _ in range(L+1)) 

    for i in range(L+1) : #row
        for j in range(L+1) : #col 
            if i==0 and j==0 : arr[i][j]=1
            else :
                if j>0 : arr[i][j] += arr[i][j-1]
                if j<i : arr[i][j] += arr[i-1][j]
                elif i<j : break
            if i==L and j==L : 
                return arr[i][j] 
print(game())



