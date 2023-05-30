import sys


def func():
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())

    room = []
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))

    # 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽이 되도록
    plus_r = [-1, 0, 1, 0]
    plus_c = [0, 1, 0, -1]

    result = 0

    # 청소되지 않은 빈 칸은 0, 벽은 1, 청소된 빈 칸은 2로 표기

    while True:
        if room[r][c] == 0:  # 현재 칸이 아직 청소되지 않은 경우
            room[r][c] = 2  # 현재 칸을 청소한다.
            result += 1

        find = False

        # 현재 칸의 주변 4 칸 중 청소되지 않은 빈 칸이 있는 경우, 반시계 방향을 우선으로 탐색한다.
        for i in range(4):
            d = (d - 1) % 4
            if room[r + plus_r[d]][c + plus_c[d]] == 0:  # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우
                r = r + plus_r[d]  # 바라보는 방향을 기준으로 한 칸 전진
                c = c + plus_c[d]

                find = True
                break

        if not find:  # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            tmp_d = (d + 2) % 4  # 바라보는 방향 기준으로 후진 (180도 회전하여 이동 후 다시 180도 회전과 동일)
            if room[r + plus_r[tmp_d]][c + plus_c[tmp_d]] != 1:  # 벽이 아니라서 한 칸 후진할 수 있다면
                r = r + plus_r[tmp_d]
                c = c + plus_c[tmp_d]
            else:
                break

    return result


print(func())
