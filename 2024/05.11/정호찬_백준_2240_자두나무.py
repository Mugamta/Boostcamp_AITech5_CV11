"""
    메모리 : 31120kb
    시간 : 56ms

    풀이 : 
        - DP를 활용
        - 예제에 대한 풀이 : 
            [초 별 열매가 떨어지는 나무 위치] 
            tree : 나무 번호
            t : 초

            tree/t 1 2 3 4 5 6 7
            1      x o o x x o o
            2      o x x o o x x

            [DP] - 이때 각 횟수에서 최댓값은 (이전 초의 현재 w까지의 값중 최댓값 + 현재 초 현재 위치에서 열매 여부)
            현재 초 현재 위치는 
                짝수번 움직였으면 -> 무조건 1번 나무
                홀수번 움직였으면 (0포함) -> 무조건 2번 나무
            
            w : 움직인 횟수
            t : 초

            t/w 0 1 2
            0   0 0 0
            1   0 1 0
            2   1 1 2
            3   2 1 3
            4   2 3 3
            5   2 4 3
            6   3 4 5
            7   4 5 6

            따라서 7초에서 최댓값이 우리가 구하려는 값
"""
import sys

input = sys.stdin.readline

# T : 초,  W : 움직일 수 있는 횟수
T, W = map(int, input().split())

# 매초 마다 떨어지는 열매 정보
tree = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

# if 1 -> 1%2 = 1, 1//2 = 0, else 2-> 2%2 = 0, 2//2= 1
dp[1][0], dp[1][1] = tree[1] % 2, tree[1] // 2
for t in range(2, T + 1):
    for w in range(W + 1):
        #움직인 횟수가 짝수(0 포함)이면
        #1번 나무임
        if not w % 2:
            p = tree[t] % 2 # 1번 나무의 열매가 있는지
        else: # 반대의 경우 2번나무임
            p = tree[t] // 2 # 2번 나무에 열매가 있는지

        #이전 초의 현재 움직인 횟수까지의 최댓값에 현재 위치 열매 여부 더하기
        dp[t][w] = max(dp[t-1][0:w+1]) + p
print(max(dp[T]))