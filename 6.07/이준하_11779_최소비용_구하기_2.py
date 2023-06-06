# 다익스트라 알고리즘
# 긴 거리에 대한 계산을 건너뛰기 위해 heapq 사용
# 최단 경로 출력
# 딕셔너리로 각 노드의 간선 표현
# 비용과 경로를 저장해야함
# 중간에 빈 숫자의 도시가 없다는 가정
# 리스트가 비어있으면, 건너뛴다...
# 경로를 저장하고, 거꾸로 출력

import heapq
import sys
input = sys.stdin.readline
# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 각 도시의 버스 정보를 저장할 딕셔너리
# 버스별 출발 도시, 도착지 도시, 비용
graph = {i : [] for i in range(1,n+1)}
for _ in range(m):
    start, end, distance = map(int, input().split())
    if graph[start] == []:
        graph[start] = [(end, distance)]
    else:
        graph[start].append((end, distance))

# 출발 도시, 도착 도시
start, end = map(int, input().split())


# 다익스트라 알고리즘
def dijkstra(start, end):
    # start 부터의 거리를 저장할 딕셔너리
    distances = {node: 100000*m for node in range(1, n+1)}
    # 처음은 0으로 초기화
    distances[start] = 0
    # 우선순위 큐
    queue = []
    # 시작 노드와 시작 노드의 거리를 우선순위 큐에 넣음
    heapq.heappush(queue, [start, distances[start]])

    path = {node: start for node in range(1, n+1)}
    while queue:
        # 현재 노드와 현재 노드까지의 거리를 가져옴
        current_node, current_distance = heapq.heappop(queue)

        # 현재 노드까지의 거리가 기존에 저장된 거리보다 크면 무시
        if distances[current_node] < current_distance:
            continue
        # 현재 노드와 연결된 노드들을 탐색하면서 비용 갱신
        for city, distance in graph[current_node]:
            distance = current_distance + distance
            if distance < distances[city]:
                distances[city] = distance
                path[city] = current_node
                heapq.heappush(queue, [city, distance])
    
    return distances[end], path

cost, r_path = dijkstra(start, end)
print(cost)
path = [end]
while path[-1] != start:
    end = r_path[end]
    path.append(end)
print(len(path))
print(*path[::-1])
