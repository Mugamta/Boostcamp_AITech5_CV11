"""
n 가지 종류의 동전 존재
각각의 동전이 의미하는 가치는 다르다

해당 동전을 적당히사용해서 가치의 합을 k로 하고싶다
각각의 동전은 몇개라도 사용할 수 있다.

그 경우의 수를 구하라
즉, 동료의 조합으로 k가치를 만들 수 있는 경우의 수를 구하라
동전 구성의 순서는 중요하지 않다
"""

n, k = map(int, input().split())
coin = [int(input()) for f in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
            
print(dp[k])