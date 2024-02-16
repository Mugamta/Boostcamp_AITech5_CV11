# https://www.acmicpc.net/problem/9205

import sys
import queue

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    store = []
    house_x, house_y = map(int, sys.stdin.readline().split())  # 상근이의 집 좌표
    for _ in range(n):  # n개의 편의점의 좌표
        x, y = map(int, sys.stdin.readline().split())
        store.append((x, y))
    festival_x, festival_y = map(int, sys.stdin.readline().split())  # 축제가 열리는 곳의 좌표

    # 문제의 목적은 상근이가 페스티벌에 행복하게 도착할 수 있는지를 판별하는 것이다.
    # 상근이가 행복하게 도착하려면 50m를 이동할 때마다 맥주를 마셔야 한다.
    # 따라서 맥주가 떨어지기 전에 편의점에 들러서 맥주를 보충하면서 페스티벌 장소로 가야한다.

    # 현재 남은 맥주의 개수 x 50m 이내에 페스티벌 좌표가 있다면 happy 출력
    # 아닐 시, 해당 범위 내에 편의점이 있는지 확인
    # 없다면 sad 출력, 있다면 해당 편의점에서 다시 확인

    q = queue.Queue()
    q.put((house_x, house_y, 0))  # 좌표, 남은 맥주의 개수, 현재 이동한 거리

    result = False

    s = set()
    for idx in range(n):  # 축제까지 도달 가능한 편의점
        if abs(store[idx][0] - festival_x) + abs(store[idx][1] - festival_y) <= 1000:
            s.add(idx)

    visit = set()

    while not q.empty() and not result:
        tup = q.get()  # 현재 좌표 x, y, 현재 맥주를 마시지 않고 이동한 거리(0 ~ 49m)

        # 맥주를 마시지 않고 추가로 이동할 수 있는 거리 + 현재 좌표에서 축제 좌표까지의 거리를 현재 맥주의 개수로 도달 가능하다면
        festival_length = abs(festival_x - tup[0]) + abs(festival_y - tup[1])

        if tup[2] + festival_length <= 1000:
            result = True
            break

        for idx in range(n):
            if idx not in visit:  # bfs를 사용하므로 방문하지 않은 편의점만 방문
                store_length = abs(store[idx][0] - tup[0]) + abs(store[idx][1] - tup[1])  # 편의점까지의 거리

                # 현재 이동거리 + 상점까지의 이동거리로 20병, 즉 1000m 이내에 존재해야 함
                if tup[2] + store_length <= 1000:
                    if idx in s:
                        result = True
                        break
                    q.put((store[idx][0], store[idx][1], (tup[2] + store_length) % 50))  # 맥주 보충 및 이동거리 갱신
                    visit.add(idx)  # 방문 표기

    if result:
        sys.stdout.write("happy\n")
    else:
        sys.stdout.write("sad\n")
