import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, arr):
    """
    goal: 탐험할 수 있는 '빈 구역의 개수' 구하기
    note:
        - 행성의 각 칸은 '숲으로 막혀 있거나, 지나갈 수 있도록 비어 있음'
        - 집이 있는 위치는 (0, 0)
        - 상, 하, 좌, 우로 이동이 가능
        - 행성은 '연결되어 있음'
    how:
        - bfs
        - '행성이 연결되어 있다는 점'을 고려하여 탐색을 수행할 것
    """
    # 전역 변수 선언
    visited = [[False] * m for _ in range(n)]
    n_empty_areas = 0
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 구현
    def bfs(_r, _c):
        visited[_r][_c] = True
        queue = deque([(_r, _c)])

        while queue:
            _r, _c = queue.popleft()
            for dr, dc in move:
                nr = _r + dr
                nc = _c + dc

                # 배열의 범위를 벗어남 >> 탐색이 가능하도록 좌표를 조정
                if nr < 0: nr = n - 1
                elif nr >= n: nr = 0
                
                if nc < 0: nc = m - 1
                elif nc >= m: nc = 0

                # 예외 1: 숲
                if arr[nr][nc] == '1':
                    continue

                # 예외 2: 이미 방문한 위치
                if visited[nr][nc]:
                    continue
                
                # 방문 처리
                visited[nr][nc] = True
                queue.append((nr, nc))


    # 탐색 로직
    for r in range(n):
        for c in range(m):
            # 예외 1: 숲
            if arr[r][c] == '1':
                continue

            # 예외 2: 이미 방문한 위치
            if visited[r][c]:
                continue

            # 탐색 && 빈 구역의 개수 업데이트
            bfs(r, c)
            n_empty_areas += 1

    return n_empty_areas


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    arr = [input().split() for _ in range(N)]

    # 함수 호출
    res = solution(N, M, arr)

    # 결과 출력
    print(res)
