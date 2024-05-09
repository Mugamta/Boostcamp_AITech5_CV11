import sys
from collections import deque
input = sys.stdin.readline

def solution(T, status, K, move):
    """
    goal: 총 K번 회전시킨 이후에 12시 방향이 S극인 톱니바퀴의 개수 출력
    note:
        - 특정 톱니바퀴(A)를 회전할 때, 옆에 있는 톱니바퀴(B)와 '서로 맞닿은 극이 다르다면', B는 A가 회전한 방향과 '반대방향'으로 회전함
        - 가장 왼쪽 톱니바퀴부터 톱니바퀴의 상태가 순서대로 주어짐
        - 상태는 8개의 정수로 이루어져 있으며, 12시 방향부터 시계방향 순서대로 주어짐
        - N극은 0, S극은 1로 나타남
        - 회전 정보의 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향(시계방향은 1, 반시계 방향은 -1)
    how:
        - 구현
        - 회전해야 할 톱니바퀴를 찾은 뒤 상태 변환(deque의 rotate 기능 활용)
    """
    # rotate 사용을 위해 deque로 자료형 변환
    status = [deque(row) for row in status]

    # 회전 알고리즘 구현
    for number, direction in move:
        # 회전해야 할 톱니바퀴 찾기
        number -= 1

        visited = [False] * T
        mem = [(number, direction)]
        
        visited[number] = True
        queue = deque([(number, direction)])
        
        while queue:
            _number, _direction = queue.popleft()

            for offset in [-1, 1]:
                new_number = _number + offset

                # 예외 1: 범위를 벗어나는 경우
                if new_number < 0 or new_number >= T:
                    continue

                # 예외 2: 이미 확인한 톱니바퀴인 경우
                if visited[new_number]:
                    continue

                # 왼쪽 톱니바퀴와 비교
                if offset == -1 and (status[_number][6] != status[new_number][2]):
                    visited[new_number] = True
                    queue.append((new_number, -_direction))

                    mem.append((new_number, -_direction))
                
                # 오른쪽 톱니바퀴와 비교
                elif offset == 1 and (status[_number][2] != status[new_number][6]):
                    visited[new_number] = True
                    queue.append((new_number, -_direction))

                    mem.append((new_number, -_direction))

        # mem 변수를 활용하여 톱니바퀴 회전
        for i, d in mem:
            status[i].rotate(d)


    # 12시 방향이 S극인 톱니바퀴의 개수 출력
    cnt = 0
    for row in status:
        if row[0] == 1:
            cnt += 1

    return cnt


if __name__ == "__main__":
    # 입력
    T = int(input())
    status = [list(map(int, input().strip())) for _ in range(T)]
    K = int(input())
    move = [list(map(int, input().split())) for _ in range(K)]
    
    # 함수 호출
    res = solution(T, status, K, move)

    # 결과 출력
    print(res)
