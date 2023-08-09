import sys
input = sys.stdin.readline

# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        # dp의 마지막 3개의 합을 dp에 추가
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009) # 1000000009로 나눈 나머지를 저장
    print(dp[n-1])