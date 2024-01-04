import sys
from collections import deque


def func():
    T = int(input())
    for _ in range(T):
        # 동전이 각각 0, 1이라고 가정할 때, 가능한 상태의 경우는 2^9
        # 테스트케이스는 최대 10개 -> 512 * 10
        # 브루트포스/백트래킹으로 해결 가능

        # 방문한 동전 표기 -> 비트마스킹으로 가능
        # 110 001 000 등의 값으로 방문 표기
        visited = [False for _ in range(512)]

        # lambda H -> 0, T -> 1 변환
        coins = [list(map(lambda x: 0 if x == 'H' else 1, input().split())) for _ in range(3)]

        # 시작 값 계산
        value = 0
        for i in range(3):
            for j in range(3):
                value += coins[i][j] * 2 ** (8 - 3 * i - j)

        # 값이 0 / 511이면 모든 비트가 0/1이므로 종료
        if value == 0 or value == 511:
            print(0)
            continue

        res = 513

        # BFS로 탐색
        dq = deque()
        dq.append((value, 0))
        visited[value] = True

        while dq:
            coin, cnt = dq.popleft()

            # 세로로 뒤집기 -> (8, 5, 2), (7, 4, 1), (6, 3, 0) 비트
            for i in range(8, 5, -1):
                tmp = coin

                for j in range(3):
                    # 특정 비트 값과의 & 연산 결과가 특정 비트가 아니라면 해당 비트가 0
                    if tmp & pow(2, i - 3 * j) != pow(2, i - 3 * j):
                        tmp |= pow(2, i - 3 * j)  # | 연산으로 비트 채움
                    else:
                        tmp -= pow(2, i - 3 * j)  # 아니라면 해당 비트 값만큼 빼면 됨

                if not visited[tmp]:
                    visited[tmp] = True
                    dq.append((tmp, cnt + 1))

                if tmp == 511 or tmp == 0:
                    res = min(res, cnt + 1)

            # 가로로 뒤집기 -> (8, 7, 6), (5, 4, 3), (2, 1, 0) 비트
            for i in range(8, 1, -3):
                tmp = coin

                for j in range(3):
                    if tmp & pow(2, i - j) != pow(2, i - j):
                        tmp |= pow(2, i - j)
                    else:
                        tmp -= pow(2, i - j)

                if not visited[tmp]:
                    visited[tmp] = True
                    dq.append((tmp, cnt + 1))

                if tmp == 511 or tmp == 0:
                    res = min(res, cnt + 1)

            # 대각선으로 뒤집기 -> (8, 4, 0)
            tmp = coin
            for i in range(8, -1, -4):
                if tmp & pow(2, i) != pow(2, i):
                    tmp |= pow(2, i)
                else:
                    tmp -= pow(2, i)

            if not visited[tmp]:
                visited[tmp] = True
                dq.append((tmp, cnt + 1))

            if tmp == 511 or tmp == 0:
                res = min(res, cnt + 1)

            # 대각선으로 뒤집기 -> (2, 4, 6)
            tmp = coin
            for i in range(2, 7, 2):
                if tmp & pow(2, i) != pow(2, i):
                    tmp |= pow(2, i)
                else:
                    tmp -= pow(2, i)

            if not visited[tmp]:
                visited[tmp] = True
                dq.append((tmp, cnt + 1))

            if tmp == 511 or tmp == 0:
                res = min(res, cnt + 1)

        if res == 513:
            print(-1)
        else:
            print(res)


func()
