"""
50 이하 -> 브루트포스, 완전탐색 등 O(N^2) 이상을 요구하는 문제가 발생할 것

키워드
인접한 네 칸 -> BFS, DFS
최소 -> 그리디, BFS 등
최소 시간 -> BFS

문제를 읽어보면, BFS로 최단시간으로 움직여야 하는 것은 맞으나, 매 분마다 물이 차는 것이 변수임
즉, BFS + 시뮬레이션 문제가 됨

물은 인접한 네 칸으로 차오르므로, 물은 최대 100번 이내로 완전히 찬다.
따라서 100번의 이동 내에 고슴도치가 길을 찾거나 이동하지 못하므로, 고슴도치의 이동은 시간에 문제가 없다.
물 또한 100 * 2500 이상이 될 수 없으므로, 250000 이내이며, 시간제한에 걸리지 않는다.

따라서 위의 알고리즘으로 해결할 수 있을 것이다.
"""
from collections import deque


def func():
    R, C = map(int, input().split())

    inp = [input() for _ in range(R)]

    maps = [[0 for _ in range(C)] for _ in range(R)]

    # 새로운 물의 위치를 저장한 후 BFS를 수행시키기 위해 저장해둘 공간 필요
    water = []

    # 두더지는 BFS로 이동해야 하므로 deque 사용
    hedgehog = deque()

    # BFS를 위해 방문한 지점 표기
    visited = [[False for _ in range(C)] for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if inp[y][x] == 'D':  # 비버의 굴과 목적지
                maps[y][x] = 2  # 도착지는 2로 설정

            elif inp[y][x] == '.':  # 이동 가능한 지점은
                maps[y][x] = 1

            elif inp[y][x] == 'S':  # 고슴도치의 시작 위치, 이동 가능 장소
                hedgehog.append((x, y))
                visited[y][x] = True  # 시작점은 방문 표기
                maps[y][x] = 1  # 시작점은 이동 가능하므로 1로 설정

            elif inp[y][x] == '*':  # 물이 차있는 지역
                water.append((x, y))
                maps[y][x] = 0  # 이동 불가능한 지역은 0으로 설정

            else:  # 나머지는 돌이므로, 물과 겹치지 않게 하기 위하여 -1으로 설정
                maps[y][x] = -1

    plus_x = (0, 0, 1, -1)
    plus_y = (1, -1, 0, 0)

    time = 0  # 걸리는 총 시간

    # 두더지가 이동할 수 있는 경로가 남아있으며, 모든 칸을 순회하지 않은 경우 반복
    while time <= R * C and hedgehog:

        # 고슴도치가 이동할 수 있는 경로에 물이 차오르면 이동 불가능하므로, 먼저 물을 BFS 시킴

        tmp_water = []  # 새로운 물의 위치를 저장해둠
        while water:
            x, y = water[-1][0], water[-1][1]
            water.pop()

            for i in range(4):
                nx, ny = x + plus_x[i], y + plus_y[i]

                # 지도를 벗어나지 않으며, 이동 가능한 칸이라면
                if 0 <= nx < C and 0 <= ny < R and maps[ny][nx] == 1:
                    tmp_water.append((nx, ny))  # 새로운 물의 위치 저장 (기존 물은 이미 BFS로 찾기 완료)
                    maps[ny][nx] = 0  # 물로 채워진 구역으로 표기

        # 이제 고슴도치의 BFS 진행
        tmp_hedgehog = deque()
        while hedgehog:
            x, y = hedgehog[0][0], hedgehog[0][1]
            hedgehog.popleft()

            for i in range(4):
                nx, ny = x + plus_x[i], y + plus_y[i]

                # 지도를 벗어나지 않으며
                if 0 <= nx < C and 0 <= ny < R:

                    # 비버의 집에 도착했다면
                    if maps[ny][nx] == 2:
                        print(time + 1)  # 걸린 시간을 출력하고 종료
                        return

                    # 방문하지 않았고, 이동 가능한 지역이라면
                    if not visited[ny][nx] and maps[ny][nx] == 1:
                        visited[ny][nx] = True  # 방문으로 표기
                        tmp_hedgehog.append((nx, ny))  # 고슴도치가 갈 수 있는 좌표 추가

        time += 1
        water = tmp_water
        hedgehog = tmp_hedgehog

    print("KAKTUS")


func()
