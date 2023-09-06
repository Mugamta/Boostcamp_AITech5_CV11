import sys

from collections import deque


def func():
    n = int(sys.stdin.readline())
    start, end = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    adjacent = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        adjacent[x].append(y)
        adjacent[y].append(x)

    visited = [False for _ in range(n+1)]
    visited[start] = True
    dq = deque([(start, 0)])
    res = - 1

    while dq:
        node, cnt = dq.popleft()
        if node == end:
            res = cnt
            break

        for next_node in adjacent[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dq.append((next_node, cnt+1))
    print(res)


func()
