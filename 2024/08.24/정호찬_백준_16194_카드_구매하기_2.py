"""
메모리 : 31120 KB
시  간 : 200 MS 

문제 주요 포인트 
    : 원하는 N은 무조건 N개 이하로 구성된 카드팩으로만 구할 수 있다
    만약 n = 5 개일때 6개로 구성된 팩이 가장 싸서 이를 사서 1개를 버리는 행위는 X

    즉, dp를 활용해볼 수 있지 않을까?
"""


import sys
input = sys.stdin.readline

n = int(input())
array = [0] +  list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if not dp[i]:
            dp[i] = dp[i-j] + array[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + array[j])
print(dp[n])
