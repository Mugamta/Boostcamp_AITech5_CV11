import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

answer = 0
temp = 0
for i in range(N) :
    temp += arr[i]
    answer += temp
print(answer)