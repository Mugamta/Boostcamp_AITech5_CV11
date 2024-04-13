import copy
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+lst[i-1][j-1]

#print(*dp, sep='\n')
maxX = -float('inf')
for s in range(1,n+1):
    for i in range(s,n+1):
        for j in range(s,n+1):
            tmp = dp[i][j] - dp[i-s][j] - dp[i][j-s] + dp[i-s][j-s]
            maxX = max(maxX, tmp)

print(maxX)
