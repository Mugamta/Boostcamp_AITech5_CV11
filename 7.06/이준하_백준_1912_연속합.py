import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i]) # arr[i] 혹은 이전 최대 연속합+arr[i]
print(max(dp))