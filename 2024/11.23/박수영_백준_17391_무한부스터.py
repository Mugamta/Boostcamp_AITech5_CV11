"""
BFS
- 최단 경로 탐색
- 목적지에 도달하기 위해 이동한 최소 격자의 개수를 구해야 함 >> 최단 경로랑 똑같음
- 최소 격자의 개수는 dp를 사용해서 기록해도 되고, queue에 담는 방식으로 기록해도 됨
"""
import sys
from collections import deque
input = sys.stdin.readline

def solution(n_row, n_col, arr):
    move = [(0, 1), (1, 0)]
    v = [[False] * n_col for _ in range(n_row)]

    queue = deque([(0, 0, 0)])
    v[0][0] = True

    while queue:
        r, c, cnt = queue.popleft()
        if (r, c) == (n_row-1, n_col-1):
            return cnt

        for booster in range(1, arr[r][c] + 1):
            for dr, dc in move:
                nr = r + dr*booster
                nc = c + dc*booster

                # 범위 벗어나면 무시
                if nr >= n_row or nc >= n_col:
                    continue

                # 방문했다면 무시
                if v[nr][nc]:
                    continue

                queue.append((nr, nc, cnt+1))
                v[nr][nc] = True
                
    return


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solution(N, M, arr)

    print(res)


if __name__ == "__main__":
    main()
