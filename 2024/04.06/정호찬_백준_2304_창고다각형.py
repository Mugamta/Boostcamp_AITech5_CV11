import sys

input = sys.stdin.readline

MAX_P = [0, 0]
N = int(input())
lst = [0 for _ in range(1001)]

for _ in range(N):
    idx, h = map(int, input().split())
    lst[idx] = h
    if MAX_P[1] < h:
        MAX_P = [idx, h]

now = 0
result = 0

#forward
for i in range(MAX_P[0] + 1):
    now = max(now, lst[i])
    result+=now

#backward
now = 0
for i in range(1000, MAX_P[0], -1):
    now = max(now, lst[i])
    result+=now

print(result)