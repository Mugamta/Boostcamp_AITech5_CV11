import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

print(arr)