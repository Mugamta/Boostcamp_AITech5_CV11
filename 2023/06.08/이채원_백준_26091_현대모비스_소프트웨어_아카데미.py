import sys
# from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

a = 0
b = N-1
answer = 0
while a < b  :
    if arr[a] + arr[b] >= M : #조건 만족시 팀 결성 
        answer += 1
        a += 1
        b -= 1
    else : #팀 결성하기에 능력치가 모자라면
        a += 1
print(answer)
