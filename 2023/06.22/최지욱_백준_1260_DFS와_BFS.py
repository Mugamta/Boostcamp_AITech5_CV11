from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    result = [str(start)]
    if start in graph:
        for v in graph[start]:
            if not visited[v]:
                result += dfs(graph, v, visited)
    return result


def bfs(graph, start, visited):
    arr =[]
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        arr.append(str(v))
        if v in graph:
            for next in graph[v]:
                if not visited[next]:
                    queue.append(next)
                    visited[next] = True
    return arr


def main():
    N, M, V = map(int, input().split())
    graph = {}

    for _ in range(M):
        a, b = map(int, input().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    for node in graph:
        graph[node].sort()

    visited = [False for _ in range(N + 1)]
    arr = dfs(graph, V, visited)
    print(' '.join(arr))
    
    visited = [False for _ in range(N + 1)]
    arr = bfs(graph, V, visited)
    print(' '.join(arr))
    
main()