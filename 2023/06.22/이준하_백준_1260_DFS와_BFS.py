from collections import deque

#dfs
def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

#bfs
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

#graph
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것을 먼저 방문
# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()
# bfs
visited = [False] * (N + 1)
bfs(V)