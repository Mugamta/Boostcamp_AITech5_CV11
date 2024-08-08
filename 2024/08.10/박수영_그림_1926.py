import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, painting):
    """
    goal:
        - 그림의 개수, 가장 넓은 그림의 넓이 구하기
        - 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0
    note:
        - 0: 색칠이 안된 부분, 1: 색칠이 된 부분
        - 1로 연결된 것을 한 그림으로 정의
        - 가로, 세로로 연결된 것만 그림임(대각선은 연결이 아님)
        - 그림의 넓이는 그림에 포함된 1의 개수임
    how:
        - BFS
        - 탐색하지 않은 지점 중 색칠이 된 부분(1)으로부터 BFS를 진행하여 클러스터링
    """
    visited = [[False] * m for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True
        
        area = 1
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in move:
                nr = r + dr
                nc = c + dc

                # 예외 1: 도화지를 벗어나는 경우
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                # 예외 2: 이미 탐색한 위치인 경우
                if visited[nr][nc]:
                    continue

                # 예외 3: 색칠이 안된 부분인 경우
                if not painting[nr][nc]:
                    continue

                area += 1
                queue.append((nr, nc))
                visited[nr][nc] = True

        return area

    # 색칠이 된 부분을 시작점으로 BFS를 수행하여 그림의 개수, 최대 넓이를 구함
    n_paintings, max_area = 0, 0
    for r in range(n):
        for c in range(m):
            if visited[r][c]: continue
            if not painting[r][c]: continue

            n_paintings += 1
            max_area = max(max_area, bfs(r, c))

    return n_paintings, max_area


if __name__ == "__main__":
    # 입력
    n, m = map(int, input().split())
    painting = [list(map(int, input().split())) for _ in range(n)]

    # 함수 호출
    res = solution(n, m, painting)

    # 결과 출력
    print(*res, sep="\n")
