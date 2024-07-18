import sys
from collections import deque
input = sys.stdin.readline

def solution(r, c, backyard):
    """
    goal: 하나의 줄에 아침까지 살아있는 양과 늑대의 수를 출력
    note:
        - '.': 비어있음
        - '#': 울타리
        - 'o': 양
        - 'v': 늑대
        - 상/하/좌/우 이동이 가능
    how:
        - BFS, 시뮬레이션
        - 같은 영역 내에 있는 양과 늑대의 수를 구한 뒤, 조건에 따라 살아남은 양과 늑대의 수를 갱신하면 됨
    """
    # 초기 양, 늑대의 수 구하기
    init_sheep, init_wolf = 0, 0
    for row in backyard:
        for e in row:
            if e == "o": init_sheep += 1
            elif e == "v": init_wolf += 1

    # BFS 알고리즘 구현
    visited = [[False] * c for _ in range(r)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(_r, _c):
        # 같은 영역 내에 있는 양과 늑대의 수
        sheep, wolf = 0, 0

        # 탐색을 위해 큐에 좌표를 저장 && 방문 처리
        queue = deque([(_r, _c)])
        visited[_r][_c] = True

        # 양 또는 늑대라면, 수를 셈
        if backyard[_r][_c] == "o": sheep += 1
        elif backyard[_r][_c] == "v": wolf += 1


        # 탐색 시작
        while queue:
            _r, _c = queue.popleft()

            for dr, dc in move:
                nr = _r + dr
                nc = _c + dc

                # 예외 1: 범위를 벗어나는 경우
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue

                # 예외 2: 울타리인 경우
                if backyard[nr][nc] == "#":
                    continue

                # 예외 3: 이미 탐색한 위치인 경우
                if visited[nr][nc]:
                    continue

                # 탐색을 위해 큐에 좌표를 저장 && 방문 처리
                queue.append((nr, nc))
                visited[nr][nc] = True

                # 양 또는 늑대라면, 수를 셈
                if backyard[nr][nc] == "o": sheep += 1
                elif backyard[nr][nc] == "v": wolf += 1
        
        return sheep, wolf

    # BFS 수행
    for _r in range(r):
        for _c in range(c):
            # 예외 1: 울타리 또는 비어있는 곳
            if backyard[_r][_c] in ["#", "."]:
                continue

            # 예외 2: 이미 탐색한 위치
            if visited[_r][_c]:
                continue

            # 같은 영역 내에 있는 양과 늑대의 수를 탐색
            s, w = bfs(_r, _c)

            # 양과 늑대의 수를 비교
            if w >= s: init_sheep -= s
            else: init_wolf -= w

    return init_sheep, init_wolf


if __name__ == "__main__":
    # 입력
    R, C = map(int, input().split())
    backyard = [list(input()) for _ in range(R)]

    # 함수 호출
    res = solution(R, C, backyard)

    # 결과 출력
    print(*res)
