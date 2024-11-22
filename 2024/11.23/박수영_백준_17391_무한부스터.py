"""
- BFS >> 최단 경로 탐색 시 사용하는 알고리즘
- 본 문제의 목표는 격자의 개수 최소화 >> 최단 경로 탐색만으로 만족할 수 없음
- 중복 탐색을 어떻게 해결할 것인가?
    - 원래는 visited 배열을 사용하는데, 본 문제에선 격자의 개수를 최소화해야 하기에
        단순 visited 배열로 판별할 수 없음 >> DP의 필요
    - DP[i][j]: (i, j) 칸에 도달하기 위해 거친 최소 격자 개수
    - 만약 (i, j) 칸에 도착했을 때, dp[i][j]보다 거친 격자 개수가 작다면 dp 배열을 갱신하고 추가 탐색
    - 격자 개수가 크다면 추가 탐색 X
"""
import sys
from collections import deque
input = sys.stdin.readline

def solution(n_row, n_col, arr):
    move = [(0, 1), (1, 0)]
    dp = [[float('inf')] * n_col for _ in range(n_row)]

    queue = deque([(0, 0, 1)])
    dp[0][0] = 1

    while queue:
        r, c, cnt = queue.popleft()

        for booster in range(1, arr[r][c] + 1):
            for dr, dc in move:
                nr = r + dr*booster
                nc = c + dc*booster

                # 범위 벗어나면 무시
                if nr >= n_row or nc >= n_col:
                    continue

                # 돌아왔다면 무시
                if dp[nr][nc] <= cnt + 1:
                    continue

                dp[nr][nc] = cnt + 1
                queue.append((nr, nc, cnt + 1))

    return dp[n_row-1][n_col-1] - 1


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solution(N, M, arr)

    print(res)


if __name__ == "__main__":
    main()
