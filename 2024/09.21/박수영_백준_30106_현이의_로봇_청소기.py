import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, k, arr):
    """
    goal: 방의 모든 영역을 청소하기 위해, 로봇 청소기를 작동시켜야 하는 *최소 횟수* 구하기
    note:
        - 로봇 청소기는 한 영역을 *청소*하고 나서 *상하좌우*로 인접한 영역 중 하나로 이동
        - 이동 조건은 두 영역 간 높이 차이가 K 이하여야 함
        - 이동 조건을 만족하지 않는 경우 *청소가 불가능* >> 이 경우 로봇 청소기의 위치를 *직접 옮겨주어야 함* >> 작동 횟수로 인식
    how:
        - BFS
        - 모든 경우의 수 탐색 불가능 >> 효율적인 탐색 필요
        - BFS 탐색을 통해 이동 가능 영역을 구분 >> 영역의 개수를 셈
    """
    visited = [[False] * m for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(_r, _c):
        queue = deque([(_r, _c)])
        visited[_r][_c] = True

        while queue:
            r, c = queue.popleft()

            for dr, dc in move:
                nr = r + dr
                nc = c + dc

                # 범위 밖
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                # 방문한 위치
                if visited[nr][nc]:
                    continue
                
                # 높이 차가 K 초과
                if abs(arr[r][c] - arr[nr][nc]) > K:
                    continue

                queue.append((nr, nc))
                visited[nr][nc] = True

    # 클러스터링
    n_area = 0

    for r in range(n):
        for c in range(m):
            if visited[r][c]:
                continue
            
            bfs(r, c)
            n_area += 1

    return n_area


if __name__ == "__main__":
    # 입력
    N, M, K = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]

    # 함수 호출
    res = solution(N, M, K, room)

    # 결과 출력
    print(res)
