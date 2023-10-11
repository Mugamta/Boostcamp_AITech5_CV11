import sys


def func():
    N = int(input())

    # N은 20이므로, N^6 = 6400만
    # 브루트 포스로 모든 경우의 수 탐색 후 풀이 가능

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    adjacent = [[] for _ in range(N*N+1)]

    plus_x = [0, 0, 1, -1]
    plus_y = [1, -1, 0, 0]

    # 여기서 1번 학생의 배치는 반드시 (2, 2)이므로 따로 빼 놓아도 됨
    for i in range(N * N):
        num, a, b, c, d = map(int, sys.stdin.readline().split())
        adjacent[num] = [a, b, c, d]

        like_cnt, blank_cnt, tmp_x, tmp_y = 0, 0, -1, -1  # 인접한 칸의 개수와 그때의 x, y 좌표
        for y in range(N):
            if like_cnt == 4:  # 인접한 칸은 최대 4개이므로, 선호 학생 칸 개수가 4개이면 더 탐색 불필요
                break

            for x in range(N):
                if like_cnt == 4:  # 인접한 칸은 최대 4개이므로, 선호 학생 칸 개수가 4개이면 더 탐색 불필요
                    break

                # 비어있는 칸 중에서 선택해야 하므로 스킵
                if matrix[y][x] != 0:
                    continue

                # 만약 아직 빈 칸을 찾지 못했다면 현재 칸을 우선 후보에 둠
                if like_cnt == 0 and blank_cnt == 0 and tmp_x == -1 and tmp_y == -1:
                    tmp_x, tmp_y = x, y

                # 선호 학생 칸, 빈 칸을 세는 임시 변수
                like_cnt_tmp, blank_cnt_tmp = 0, 0

                # 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정하므로, 인접한 칸의 좋아하는 학생 수를 계산
                for idx in range(4):
                    nx = x + plus_x[idx]
                    ny = y + plus_y[idx]

                    # 배치도를 벗어난다면 무시
                    if 0 > nx or N <= nx or 0 > ny or N <= ny:
                        continue

                    # 인접한 칸에 좋아하는 학생이 있다면 선호 칸 개수 1 증가
                    if matrix[ny][nx] in adjacent[num]:
                        like_cnt_tmp += 1

                    # 이 칸이 비었다면 빈 칸 개수 1 증가
                    if matrix[ny][nx] == 0:
                        blank_cnt_tmp += 1

                # 좋아하는 학생이 더 많이 인접했거나, 좋아하는 학생 수는 같지만 빈 칸이 더 많은 경우 갱신
                # (조건 3번은 for문의 순회 순서 및 36번째 줄에서 자동적으로 처리됨)
                if like_cnt_tmp > like_cnt or (like_cnt_tmp == like_cnt and blank_cnt_tmp > blank_cnt):
                    like_cnt = like_cnt_tmp
                    blank_cnt = blank_cnt_tmp
                    tmp_x = x
                    tmp_y = y

        matrix[tmp_y][tmp_x] = num

    res = 0  # 만족도
    for y in range(N):
        for x in range(N):

            cnt = 0  # 인접한 칸의 개수를 세는 변수
            for idx in range(4):
                nx = x + plus_x[idx]
                ny = y + plus_y[idx]

                # 배치도를 벗어난다면 무시
                if 0 > nx or N <= nx or 0 > ny or N <= ny:
                    continue

                # 인접한 칸에 좋아하는 학생이 있다면 선호 칸 개수 1 증가
                if matrix[ny][nx] in adjacent[matrix[y][x]]:
                    cnt += 1

            if cnt != 0:  # cnt가 0이면 학생의 만족도는 0
                res += 10 ** (cnt-1)  # cnt가 이면 1, 2이면 10, 3이면 100, 4이면 1000

    print(res)


func()
