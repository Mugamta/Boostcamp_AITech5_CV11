import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def solution(n, m, arr):
    """
    goal: 얻을 수 있는 *안전 영역*의 *최대 크기* 구하기
    note:   
        - 0: 빈칸, 1: 벽, 2: 바이러스
        - 바이러스는 상하좌우로 인접한 *빈칸*으로 모두 퍼져나갈 수 있음
        - 새로 세울 수 있는 벽의 개수는 3개이며, *꼭 3개를 세워야 함.*
    how:
        - 시뮬레이션
        - 벽을 세울 수 있는 위치 중 3개를 뽑아 새로운 지도를 만든 뒤, BFS를 돌려서 안전 영역을 계산함
    """
    # 벽을 세울 수 있는 위치, 바이러스 위치 구하기
    empty_pos = []
    virus_pos = []

    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0:
                empty_pos.append((r, c))

            elif arr[r][c] == 2:
                virus_pos.append((r, c))

    # 벽을 세우기 이전의 안전영역 계산하기
    init_safety_area = len(empty_pos)

    # empty_pos에서 3개씩 뽑기
    new_walls = list(combinations(empty_pos, 3))

    def bfs(arr_cp):
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * m for _ in range(n)]

        # 바이러스 위치를 방문 처리
        queue = deque(virus_pos)
        for r, c in virus_pos:
            visited[r][c] = True

        # 초기 안전영역에서 새로 세운 벽 개수만큼 빼야함
        area = init_safety_area - 3

        # BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in move:
                nr = r + dr
                nc = c + dc

                # 범위 벗어나거나
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                # 벽이거나
                if arr_cp[nr][nc] == 1:
                    continue
                
                # 과거에 방문했었다면 무시
                if visited[nr][nc]:
                    continue
                
                # 바이러스 퍼뜨리고, 안전영역을 줄임
                queue.append((nr, nc))
                visited[nr][nc] = True

                area -= 1

        return area

    # 시뮬레이션 진행
    safety_area = float('-inf')
    for walls in new_walls:
        arr_cp = [row[:] for row in arr] # 복사
        for r, c in walls:
            arr_cp[r][c] = 1 # 벽 세우기

        # 안전영역 넓이 구하기
        area = bfs(arr_cp)

        if area > safety_area:
            safety_area = area

    return safety_area


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 함수 호출
    res = solution(N, M, arr)

    # 결과 출력
    print(res)
