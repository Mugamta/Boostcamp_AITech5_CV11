import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, area):
    """
    goal: 아군 위력의 합과 적군 위력의 합 구하기 (공백을 두고 순서대로 출력)
    note:
        - 아군은 흰색 옷을, 적군은 파란색 옷을 착용하고 있음
        - 같은 팀의 병사들은 모이면 모일수록 강해짐(N명이 모여있다면 N**2의 위력)
        - 상, 하, 좌, 우에 인접한 경우 모인 것으로 간주함
    how:
        - BFS
        - 방문하지 않은 위치를 시작점으로 잡고, 클러스터링 수행
        - 아군과 적군의 위력을 따로 누적
    """
    # 방문 여부를 기록할 배열 선언
    visited = [[False] * N for _ in range(M)]

    # 아군과 적군의 위력을 누적할 변수 선언
    white_power, blue_power = 0, 0

    # 탐색 범위 설정
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 구현
    def bfs(_r, _c):
        queue = deque([(_r, _c)])
        visited[_r][_c] = True

        cnt = 1 # 그룹 내 사람의 숫자를 세기 위한 변수 선언
        while queue:
            r, c = queue.popleft()

            for dr, dc in move:
                nr = r + dr
                nc = c + dc

                # 예외 1: 범위를 벗어나는 경우
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # 예외 2: 이미 탐색한 지점인 경우
                if visited[nr][nc]:
                    continue

                # 예외 3: 다른 그룹인 경우
                if area[r][c] != area[nr][nc]:
                    continue

                # 큐에 추가 + 방문 처리 + cnt 증가
                queue.append((nr, nc))
                visited[nr][nc] = True
                cnt += 1

        return cnt**2

    # 방문하지 않은 위치를 시작점으로 잡고, 클러스터링 수행
    for r in range(m):
        for c in range(n):
            if not visited[r][c]:
                power = bfs(r, c)

                if area[r][c] == 'W':
                    white_power += power
                elif area[r][c] == 'B':
                    blue_power += power

    return (white_power, blue_power)


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    area = [list(input()) for _ in range(M)]

    # 함수 호출
    res = solution(N, M, area)

    # 결과 출력
    print(*res)
