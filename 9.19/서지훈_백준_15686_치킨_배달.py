import sys


def func():
    N, M = map(int, input().split())
    city = []
    for _ in range(N):
        city.append(list(map(int, sys.stdin.readline().split())))

    houses = []
    chickens = []
    for y in range(N):
        for x in range(N):
            if city[y][x] == 1:
                houses.append((x, y))
            elif city[y][x] == 2:
                chickens.append((x, y))

    res = len(houses) * N * 2  # 집의 개수 * 최대 치킨 거리 (2N-2)보다 큰 값

    for i in range(2**(len(chickens))):  # 2^치킨집의 개수만큼 경우의 수를 만듬
        visited = []

        for j in range(len(chickens)):
            visited.append(0 if i % 2 == 0 else 1)
            i //= 2

        if sum(visited) != M:  # 치킨집이 M개가 남아야 하므로, 아닌 경우는 스킵
            continue

        city_chicken_distance = 0
        for house_x, house_y in houses:

            tmp = 2 * N  # 각 집에서 가장 가까운 치킨집의 거리를 구함

            for idx, (chicken_x, chicken_y) in enumerate(chickens):
                if visited[idx] == 1:
                    tmp = min(tmp, abs(house_x - chicken_x) + abs(house_y - chicken_y))

            city_chicken_distance += tmp  # 이를 도시의 치킨 거리에 더해줌

        res = min(res, city_chicken_distance)  # 현재까지의 도시의 최소 치킨 거리 갱신

    print(res)


func()
