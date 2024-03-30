"""
문제의 조건에서 특별한 알고리즘은 보이지 않음
-> 2차원 배열, 방향, 퍼즐... 시뮬레이션?
"""
from itertools import product

def rotate(x, y, cnt, target, length):
    if y > 0:  # 위칸
        target[y - 1][x] = (target[y - 1][x] + cnt) % 4
    if x > 0:  # 좌측칸
        target[y][x - 1] = (target[y][x - 1] + cnt) % 4
    if x < length - 1:  # 우측 칸
        target[y][x + 1] = (target[y][x + 1] + cnt) % 4
    if y < length - 1:  # 아래 칸
        target[y + 1][x] = (target[y + 1][x] + cnt) % 4
    # 중앙 칸
    target[y][x] = (target[y][x] + cnt) % 4

def solution(clockHands):
    answer = 4**64
    
    # 1. length * length 크기의 정사각형이 존재하며, 각 정사각형의 셀에는 0 ~ 3으로 북동남서의 방향이 표현된다.
    length = len(clockHands)

    # 2. 모든 시곗바늘이 12시 방향을 가르키면 퍼즐이 해결되며, 이것이 목표이다.
    # 3. 시곗바늘을 돌리면 그 시계의 상하좌우로 인접한 시계들의 시계바늘도 함께 돌아간다.
    # 4. 최소한의 조작으로 퍼즐을 해결하기 위한 방법은?
    
    # 문제의 조건이 작으므로 백트래킹?
    # 각 칸은 회전의 경우의 수는 4이므로, 4^64의 경우의 수가 존재함...
    # 이를 줄이거나 다른 알고리즘 찾기?
    
    # 가장 위 행을 회전시킨 결과가 주어진다고 가정하자.
    # 이 경우, 두 번째 행은 첫 번째 행에 영향을 주므로 0을 만들기 위하여 가능한 경우가 고정된다.
    # 마찬가지로, 아래 행들은 위 행에 영향을 주므로 0을 가능한 경우가 고정된다.
    # 즉, 위의 행이 없는 첫 번째 행만 고정시키면 된다.
    # 따라서 경우의 수는 최대 4^8으로 첫 번째 행을 고려하면 된다.
    # 이후, 나머지 행들은 위의 행의 결과에 따라 종속되므로 짧은시간 내에 결정 가능하다.
    
    li = [i for i in range(4)]
    
    # product로 중복 순열을 만들기
    selects = list(product(li, repeat = length))  # 숫자의 범위는 li, 수열의 길이는 length
    
    # select는 length의 길이로 첫 행의 회전을 결정함
    t = 0
    for select in selects:
        
        # 기존 방향이 담긴 값
        tmp_clockHands = [clockHands[i][:] for i in range(length)]
        
        # 첫 번째 행을 먼저 회전
        for x in range(length):
            rotate(x, 0, select[x], tmp_clockHands, length)
        
        cnt = sum(select)
        # 이제 두 번째 행부터, 첫 번째 행을 0으로 채우기 위하여 회전값을 더함
        for y in range(1, length):
            for x in range(length):
                # 위 칸이 0이라면 건드리지 않음
                if tmp_clockHands[y - 1][x] == 0:
                    continue
                
                # 위 칸이 0이 아니라면 그 횟수만큼 현재 칸의 회전 필요
                cnt += (4 - tmp_clockHands[y - 1][x]) % 4
                rotate(x, y, (4 - tmp_clockHands[y - 1][x]) % 4, tmp_clockHands, length)
        
        # 만약 모든 행의 합이 0이라면 (퍼즐을 풀었다면) 이때의 조작 횟수 중 최소값으로 저장
        if sum([sum(tmp_clockHands[i]) for i in range(length)]) == 0:
            answer = min(answer, cnt)
    
    return answer