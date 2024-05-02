"""
    메모리 : 31120 kb
    시간 : 40 ms
"""
import sys

input = sys.stdin.readline


N = int(input())
switches = list(map(int, input().split()))
S_N = int(input())

for _ in range(S_N):
    gender, num = map(int, input().split())

    if (gender == 1):
        for i in range(num, N+1, num):
            switches[i - 1] = int(not switches[i - 1])
    else:
        middle = num - 1
        switches[middle] = int(not switches[middle])

        left, right = middle - 1, middle + 1
        while (left >= 0 and right < N and (switches[left] == switches[right])):
            switches[left], switches[right] = int(not(switches[left])), int(not(switches[right]))
            left-=1
            right+=1

for n in range(0, N+1, 20):
        print(*switches[n:n+20])