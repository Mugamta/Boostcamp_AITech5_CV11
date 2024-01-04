from collections import deque
import sys

N, M, V = map(int, input().split())

adjacent = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjacent[a][b] = True
    adjacent[b][a] = True
visited = [False for _ in range(N + 1)]


def dfs(start):
    sys.stdout.write(str(start) + " ")
    visited[start] = True
    for i in range(1, N + 1):
        if not visited[i] and adjacent[start][i]:
            dfs(i)


def bfs(start):
    visited2 = [False for _ in range(N + 1)]
    visited2[start] = True
    dq = deque()
    dq.append(V)
    while dq:
        start = dq.popleft()
        sys.stdout.write(str(start) + " ")
        for i in range(1, N + 1):
            if not visited2[i] and adjacent[start][i]:
                dq.append(i)
                visited2[i] = True


dfs(V)
sys.stdout.write("\n")
bfs(V)
