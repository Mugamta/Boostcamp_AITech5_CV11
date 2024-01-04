import sys
from decimal import Decimal


# 최단거리는 비교만 하면 되므로 굳이 제곱근을 사용해서 정확도를 낮출 필요 없음
def get_distance(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def func():
    N = int(input())
    locates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    X_H, Y_H = map(int, sys.stdin.readline().split())

    # 임의의 각도에서 시작하여 반시계 방향으로 돌면서, 자신과 정면에 있는 사람의 좌표를 기록
    # 혁이의 y 좌표를 기준으로, y = Y_H인 선을 하나 그음  (임의의 선이라도 상관 없음)
    # 다른 사람들의 좌표 (X, Y)와 혁이의 좌표 (X_H, Y_H)를 잇는 선을 그음
    # 두 선이 이루는 각도와 거리를 계산해두고, 각도와 거리를 기준으로 오름차순 정렬하면 됨

    # 기울기로 기준으로 계산 -> 같은 x, y좌표가 존재하는 경우 구별할 수 없음
    # 따라서 혁이의 위치를 원점으로 생각하여 각각 어느 사분면에 존재하는지 구함
    # 이후, 1 -> 2 -> 3 -> 4 사분면의 순서로 이동하며 출력하되,
    # +축 -> 1 사분면 -> +y축 -> 2사분면 -> -x축 -> 3사분면 -> -y축 -> 4 사분면 순으로 출력

    quadrants = [[], [], [], []]  # 4개를 만들어 0 ~ 3 사분면 활용
    axis = [[], [], [], []]  # +x, +y, -x, -y
    for X, Y in locates:
        dx = X - X_H
        dy = Y - Y_H

        if dx == 0 or dy == 0:  # 축 위에 있는 경우
            if dx > 0:
                axis[0].append([X, Y])  # +x 축
            elif dy > 0:
                axis[1].append([X, Y])  # +y 축
            elif dx < 0:
                axis[2].append([X, Y])  # -x 축
            else:
                axis[3].append([X, Y])  # -y 축
        else:
            if dx > 0 and dy > 0:
                quadrants[0].append([X, Y])
            elif dx < 0 and dy > 0:
                quadrants[1].append([X, Y])
            elif dx < 0 and dy < 0:
                quadrants[2].append([X, Y])
            else:
                quadrants[3].append([X, Y])

    # 이제 사분면은 기울기와 거리를 기준으로, 축은 거리를 기준으로 정렬
    # +축 -> 1 사분면 -> +y축 -> 2사분면 -> -x축 -> 3사분면 -> -y축 -> 4 사분면으로 사용할 예정
    # 1, 3 사분면은 x축에서 시작하므로 오름차순
    quadrants[0].sort(key=lambda x: (abs(Decimal(Decimal(x[1] - Y_H) / Decimal(x[0] - X_H))), (x[0] - X_H)**2 + (x[1] - Y_H)**2))
    quadrants[2].sort(key=lambda x: (abs(Decimal(Decimal(x[1] - Y_H) / Decimal(x[0] - X_H))), (x[0] - X_H)**2 + (x[1] - Y_H)**2))

    # 2, 4 사분면은 4축에서 시작하므로 내림차순
    quadrants[1].sort(key=lambda x: (-abs(Decimal(Decimal(x[1] - Y_H) / Decimal(x[0] - X_H))), (x[0] - X_H)**2 + (x[1] - Y_H)**2))
    quadrants[3].sort(key=lambda x: (-abs(Decimal(Decimal(x[1] - Y_H) / Decimal(x[0] - X_H))), (x[0] - X_H)**2 + (x[1] - Y_H)**2))

    for i in range(4):
        axis[i].sort(key=lambda x: (x[0] - X_H)**2 + (x[1] - Y_H)**2)

    # +축 -> 1 사분면 -> +y축 -> 2사분면 -> -x축 -> 3사분면 -> -y축 -> 4 사분면 순으로 출력
    for i in range(4):
        for X, Y in axis[i]:
            sys.stdout.write(str(X) + " " + str(Y) + "\n")

        for X, Y in quadrants[i]:
            sys.stdout.write(str(X) + " " + str(Y) + "\n")


func()
