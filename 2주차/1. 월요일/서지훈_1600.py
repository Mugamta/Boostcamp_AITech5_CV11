"""
문제 링크 : https://www.acmicpc.net/problem/1600
제출 내역 : https://www.acmicpc.net/status?from_mine=1&problem_id=1600&user_id=mugamta

풀이 내역

1. 아이디어 접근
최단 거리이고 가중치가 없으므로 BFS로 접근함
단, K번까지는 체스의 나이트처럼 움직일 수 있음
Queue의 원소에 위치 조건과 이동횟수 뿐만 아니라 나이트처럼 움직인 횟수를 기록하여 탐색으로 코드 작성

17분째 - 3% 구간에서 실패
원인은 나이트처럼 이동하는 것과 그냥 이동하는 것을 하나의 배열에서 확인했기 때문

28분째에 수정했으나 바로 시간초과 발생

31분째에 isited[k+1][tmp_y][tmp_x] 조건이 잘못된걸 수정 - 40% 에서 시간초과 발생

34분째에 queue에 추가하기 전 다음 위치가 종료 지점이면 멈추도록 함 - 40% 에서 시간초과 발생
35분째에 sys.stdin.readline으로 수정 - 40% 에서 시간초과 발생
43분째에 visited를 false/true로 하는 대신 도달한 시간을 줄여나가는 방식 사용 - 40% 에서 시간초과 발생
    BFS를 이용하므로 이는 사용할 필요 없음

57분째에 함수로 변경 - 시간초과 대신 96%에서 오답 발생
    함수 사용이 더 빠른 이유 : https://8iggy.tistory.com/155를 참조
    요약하자면, 전역 변수들은 dictionary에 저장/읽기 되고, 로컬 변수는 고정크기 array에 저장된다.
    dictionary는 hash table을 이용하므로 추가적인 연산이 필요할 것이고, 당연히 array보다 느리다.
    따라서 동일한 코드는 함수를 구현하여 사용하는 것이 더 빠르다. - 파이썬의 특징

63분째에 W = H = 1인 엣지 케이스에서, 보드의 유일한 칸이 1이면 탐색하지 않는 문제를 수정하여 정답

수정 : deque > list > queue의 속도로 속도가 빠름
    원인 : queue는 멀티 스레드를 위해 만들어진 라이브러리인 반면,
            deque와 list는 일반적인 자료구조의 형태
    따라서 싱글스레드 환경(코딩테스트)에서는 queue 대신 deque를 사용하자.

"""
from collections import deque
import sys


def bfs():
    K = int(input())

    W, H = map(int, sys.stdin.readline().split())

    board = []
    for h in range(H):
        board.append(list(map(int, sys.stdin.readline().split())))

    if W == 1 and H == 1:
        return 0

    dq = deque()
    dq.append((0, 0, 0, 0))  # x좌표, y좌표, 나이트처럼 움직인 횟수, 총 동작 횟수
    visited = [[[False for i in range(W)] for j in range(H)] for k in range(K + 1)]

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    knight_plus_x = [1, 2, 2, 1, -1, -2, -2, -1]
    knight_plus_y = [2, 1, -1, -2, -2, -1, 1, 2]

    while dq:
        tup = dq.popleft()
        x = tup[0]
        y = tup[1]
        k = tup[2]
        time = tup[3]

        if k < K:
            for i in range(8):
                tmp_x = x + knight_plus_x[i]
                tmp_y = y + knight_plus_y[i]

                if 0 <= tmp_x < W and 0 <= tmp_y < H and board[tmp_y][tmp_x] == 0 and not visited[k + 1][tmp_y][tmp_x]:

                    if tmp_x == W - 1 and tmp_y == H - 1:
                        return time + 1

                    visited[k + 1][tmp_y][tmp_x] = True
                    dq.append((tmp_x, tmp_y, k + 1, time + 1))

        for i in range(4):
            tmp_x = x + plus_x[i]
            tmp_y = y + plus_y[i]

            if 0 <= tmp_x < W and 0 <= tmp_y < H and board[tmp_y][tmp_x] == 0 and not visited[k][tmp_y][tmp_x]:
                if tmp_x == W - 1 and tmp_y == H - 1:
                    return time + 1

                visited[k][tmp_y][tmp_x] = True
                dq.append((tmp_x, tmp_y, k, time + 1))
    return -1


print(bfs())
