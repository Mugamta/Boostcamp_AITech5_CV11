import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, paper):
    """
    goal: 도화지에 그려져 있는 그림의 개수와 그림 중 가장 넓이가 넓은 그림의 넓이 구하기
    note:
        - '0': 색칠이 안된 부분
        - '1': 색칠이 된 부분
        - 그림: 1로 연결된 것(가로 또는 세로, 대각선은 해당 없음)
        - 그림의 넓이: 그림에 포함된 1의 개수
    how:
        - BFS
    """
    # 그림의 개수, 넓이(가장 넓은 그림의)
    n_painting, area = 0, 0

    # 방문 처리를 위한 배열 선언
    visited = [[False] * m for _ in range(n)]

    # 이동 방향
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 구현
    def bfs(_r, _c):
        queue = deque([(_r, _c)])
        visited[_r][_c] = True

        area_tmp = 1 # 그림 한 개의 넓이

        while queue:
            r, c = queue.popleft()

            for dr, dc in move:
                nr = r + dr
                nc = c + dc

                # 예외 1: 범위를 벗어난 경우
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                # 예외 2: 색칠이 안된 부분
                if not paper[nr][nc]:
                    continue

                # 예외 3: 이미 탐색한 지점
                if visited[nr][nc]:
                    continue
                
                # 연결된 지점을 큐에 추가
                queue.append((nr, nc))
                visited[nr][nc] = True

                area_tmp += 1 # 그림의 넓이 증가

        # 현재 그림의 넓이가 가장 넓은 경우, area를 갱신
        nonlocal area

        if area_tmp > area:
            area = area_tmp
        

    # 탐색 로직 구현
    for r in range(n):
        for c in range(m):
            # 예외 1: 색칠이 안된 부분
            if not paper[r][c]:
                continue

            # 예외 2: 이미 탐색한 지점
            if visited[r][c]:
                continue
            
            # BFS 수행 후 그림의 개수를 증가
            bfs(r, c)
            n_painting += 1

    return n_painting, area


if __name__ == "__main__":
    # 입력
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]

    # 함수 호출
    res = solution(n, m, paper)

    # 결과 출력
    print(*res, sep='\n')
