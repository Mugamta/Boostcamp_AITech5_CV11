import sys


def recursion(n, x, y):
    # 1. 모든 픽셀이 일치한다면 숫자 하나만 기재함

    check = video[y][x]  # 첫 번째 픽셀의 값

    for i in range(y, y + n):  # 현재 구역 전체를 탐색하며 모든 픽셀의 일치 여부 판단
        for j in range(x, x + n):
            if check != video[i][j]:  # 모든 구역이 일치하는 것은 아님 - 분할하여 탐색 필요

                # 2. 픽셀이 다른 구역이 존재한다면, 네 가지 구역으로 나누어서 기재
                sys.stdout.write("(")  # 일치하지 않는 구역은 괄호로 구분됨

                recursion(n // 2, x, y)  # 왼쪽 위
                recursion(n // 2, x + n // 2, y)  # 오른쪽 위
                recursion(n // 2, x, y + n // 2)  # 왼쪽 아래
                recursion(n // 2, x + n // 2, y + n // 2)  # 오른쪽 아래

                sys.stdout.write(")")

                return  # 픽셀이 다른 구역이면 여기서 종료

    # 모든 픽셀이 일치하는 경우는 숫자 하나만 기재함
    if check == '0':
        sys.stdout.write('0')
    else:
        sys.stdout.write('1')


N = int(input())
video = [input() for i in range(N)]
recursion(N, 0, 0)