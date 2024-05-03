"""
    메모리 : 35364kb
    시간 : 184ms
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
arr.sort()

tmp = 2000000000
left, right = 0, 1
while (right < N):
    diff = arr[right] - arr[left]
    if (diff== M):
        tmp = M
        break
    elif (diff > M):
        tmp = min(tmp, diff)
        left+=1
    else:
        right+=1

print(tmp)