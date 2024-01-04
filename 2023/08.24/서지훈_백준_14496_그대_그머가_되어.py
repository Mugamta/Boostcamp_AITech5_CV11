"""
우리는 a를 b로 바꾸고 싶다.
하지만 a에서 c로, c에서 d로, d에서 a로 가는 등 바로 바꿀 수 있다는 보장이 없다.
이 중 최소 횟수를 구해야 한다.

즉, 시작점 a에서 b로 도착하는 최단 거리를 구하는 문제이다.
이 문제는 별도의 가중치가 없으므로 BFS로 풀 수 있다.

정점의 개수는 최대 1000이고, 간선의 개수는 최대 10000이다.
따라서 인접 행렬, 인접 리스트, 간선 리스트 중 무엇을 이용해도 메모리 초과는 발생하지 않는다.
"""

from collections import deque


def bfs():
    a, b = map(int, input().split())
    N, M = map(int, input().split())

    li = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        li[x].append(y)
        li[y].append(x)

    if a == b:
        return 0

    dq = deque([(a, 1)])

    visited = [False for _ in range(N+1)]
    visited[a] = True

    while dq:
        locate, res = dq.popleft()

        for i in li[locate]:
            if i == b:
                return res

            if not visited[i]:
                visited[i] = True
                dq.append((i, res+1))

    return -1


print(bfs())
