"""
    메모리 : 32140 KB
    시  간 : 480 MS
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = 1
result = 0

while right <= n and left <= right:
    temp = sum(array[left:right])

    if temp == m:
        result += 1
        left+=1
    elif temp > m:
        left += 1
    else:
        right += 1

print(result)
