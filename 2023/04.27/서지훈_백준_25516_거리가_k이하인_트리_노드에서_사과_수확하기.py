import sys
sys.setrecursionlimit(1000000)


def dfs(node, distance):
    if k > distance:
        for next_node in adjacent[node]:
            if not visited[next_node]:
                visited[next_node] = True
                global result
                result += apples[next_node]
                dfs(next_node, distance+1)


n, k = map(int, input().split())
adjacent = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().split())
    adjacent[p].append(c)
    adjacent[c].append(p)
apples = list(map(int, sys.stdin.readline().split()))


visited = [False for _ in range(n)]
visited[0] = True
result = apples[0]

dfs(0, 0)

print(result)