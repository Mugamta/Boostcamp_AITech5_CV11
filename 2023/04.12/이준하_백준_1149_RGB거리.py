"""
2:25 문제 풀이 시작
2:28 세번째 조건이 다 포함하는거 아닌가??
2:35 for 문 돌면서 조건에 맞게 칠하는 비용을 더해봄 (그리디)
2:50 가능한 모든 경우를 다 해보고 최소를 출력 (dp)
2:58 테스트케이스 성공
2:59 성공!
"""
import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))



