# 그리디 정렬 투포인터

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = 0
for i in range(n // 2):
    if a[i] + a[n-1-i] >= m:
        answer += 1
print(answer)

