import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, area):
    """
    goal: 무너진 건물의 개수와 무너지지 않은 건물의 개수 구하기
    note:
        - 진원지에서 발생한 지진을 본진, 건물이 무너졌을 때 발생하는 지진을 여진
        - 본진은 진원지를 기준으로 상하좌우 각 방향으로 2칸까지 뻗어나가며, 여진은 1칸까지 뻗어나감
        - 본진과 여진은 건물에 영향을 줌
        - 내진 설계가 되어 있지 않은 건물은 지진이 도달한 즉시 무너지지만, 내진 설계가 되어 있는 건물은 지진이 2번 도달하면 무너짐
        - 본진과 여진이 뻗어나가는 도중 지진 방파제를 만나거나 격자 모양의 지역 밖으로 나가면 더 이상 뻗어나가지 않음
        - '@': 진원지, '.': 일반 도로, '*': 일반 건물, '#': 내진 설계 건물, '|': 방파제
    how:
        - BFS를 활용한 구현
        - 건물의 상태(damage)를 기반으로 탐색함
    """
    # 진원지 찾기
    start = (0, 0)
    for r in range(N):
        for c in range(M):
            if area[r][c] == '@':
                start = (r, c)
                break

    # BFS 구현                
    # 본진 범위를 큐에 담기
    damage = [[0] * M for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque() # 붕괴 예정 건물의 좌표만 저장
    for dr, dc in move:
        for i in range(1, 3):
            nr = start[0] + dr*i
            nc = start[1] + dc*i

            # 예외 1: 지역을 벗어나는 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                break

            # 예외 2: 방파제를 만난 경우
            if area[nr][nc] == '|':
                break

            # 도로인 경우 다음 범위로 이동
            if area[nr][nc] == '.':
                continue
            
            # 건물 상태(damage)를 업데이트하고, 일반 건물인 경우 큐에 추가
            damage[nr][nc] += 1
            if area[nr][nc] == '*':
                queue.append((nr, nc))

    while queue:
        # 큐에서 꺼내는 순간 붕괴
        _r, _c = queue.popleft()
        area[_r][_c] = 'X'

        # 여진 발생
        for dr, dc in move:
            nr = _r + dr    
            nc = _c + dc

            # 예외 1: 지역을 벗어나는 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 예외 2: 방파제를 만난 경우
            if area[nr][nc] == '|':
                continue

            # 예외 3: 도로인 경우
            if area[nr][nc] == '.':
                continue

            # 일반 건물을 만났을 때
            if area[nr][nc] == '*':
                if damage[nr][nc]: # 붕괴될 예정이라면 탐색 X
                    continue

                damage[nr][nc] += 1
                queue.append((nr, nc))

            # 내진 설계 건물을 만났을 때
            if area[nr][nc] == '#':
                if damage[nr][nc] >= 2: # 붕괴될 예정이라면 탐색 X
                    continue

                damage[nr][nc] += 1
                if damage[nr][nc] == 2:
                    queue.append((nr, nc))
            

    # 무너진 건물과 무너지지 않은 건물의 개수 구하기
    cnt_dead, cnt_live = 0, 0
    for r in range(N):
        for c in range(M):
            if area[r][c] == 'X':
                cnt_dead += 1

            elif area[r][c] in ['*', '#']:
                cnt_live += 1

    return cnt_dead, cnt_live


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    area = [list(input()) for _ in range(N)]
    
    # 함수 호출
    res = solution(N, M, area)

    # 결과 출력
    print(*res)
