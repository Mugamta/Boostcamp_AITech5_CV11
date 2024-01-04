import sys
sys.setrecursionlimit(1000000)


def dfs(node):
    for next_node in adjacent[node]:
        if not visited[next_node]:
            visited[node] = True
            parent[next_node] = node
            dfs(next_node)


N = int(input())
adjacent = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

parent = [0] * (N+1)
visited = [False] * (N+1)
visited[1] = True
dfs(1)

for i in range(2, N+1):
    sys.stdout.write(str(parent[i]) + "\n")