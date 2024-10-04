"""
누적합 문제

# [0 2 0 0 0 -2]
# 누적합 실행시 -> [0 2 2 2 2 0]
# 만약 여러개 라면
# [0 0 0 0 0 0]
# (1, 3) += 2, (2, 4) += 3, (1, 4) -= 2
# [0 2 2 2 0 0] -> [0 2 5 5 3 0] -> [0 0 3 3 1 0]
# 누적합 
# [0 0 3 0 -2 -1 0] -> 누적합 -> [0 0 3 3 1 0 0]
# [한번의 합연산으로 전부 합가는 -> 구간 합은 누적합으로 해결]

누적합 추천 문제
https://school.programmers.co.kr/learn/courses/30/lessons/92344
카카오 2022 블라인드 테스트 : 파괴되지 않는 건물
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grounds = list(map(int, input().split()))
dp = [0] * (N + 1)
for _ in range(M):
    s, e, h = map(int, input().split())
    dp[s-1] += h
    dp[e] -= h

tmp = 0
for i in range(len(grounds)):
    dp[i] = dp[i] + tmp
    grounds[i] += dp[i]
    tmp = dp[i]
    
print(*grounds)
