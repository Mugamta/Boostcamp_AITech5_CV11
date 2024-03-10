import sys


def func():
    A, B = map(int, sys.stdin.readline().split())
    N, M = map(int, sys.stdin.readline().split())

    lands = [[0 for _ in range(A + 1)] for _ in range(B + 1)]

    d = {'N': 0, 'E': 1, 'S': 2, 'W': 3}  # 북동남서의 시계방향으로 설정

    robots = [[0, 0, 0]]  # 로봇의 현재 위치를 저장
    for i in range(1, N + 1):
        x, y, direction = sys.stdin.readline().split()
        x, y = int(x), int(y)

        robots.append([x, y, d[direction]])
        lands[y][x] = i  # 각 위치에 로봇이 존재함을 표기

    plus_x = [0, 1, 0, -1]
    plus_y = [1, 0, -1, 0]

    for _ in range(M):
        idx, operation, cnt = sys.stdin.readline().split()
        idx, cnt = int(idx), int(cnt)

        x, y, direction = robots[idx]

        # L, R에 따라 방향 전환
        if operation == 'L':
            robots[idx] = x, y, (direction - cnt) % 4
        elif operation == 'R':
            robots[idx] = x, y, (direction + cnt) % 4
        else:
            while cnt > 0:
                nx, ny = x + plus_x[direction], y + plus_y[direction]

                if 1 <= nx <= A and 1 <= ny <= B:
                    if lands[ny][nx] != 0:  # 로봇이 있는 위치라면
                        print("Robot {} crashes into robot {}".format(idx, lands[ny][nx]))
                        return

                    lands[y][x] = 0
                    x, y = nx, ny
                    lands[y][x] = idx

                else:
                    print("Robot {} crashes into the wall".format(idx))
                    return

                cnt -= 1

            # 최종 좌표를 덮어씌움
            robots[idx] = x, y, direction

    print("OK")


func()
