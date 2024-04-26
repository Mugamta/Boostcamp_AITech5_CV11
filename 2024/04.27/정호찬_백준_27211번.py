"""
너비 우선 탐색으로 구역내에서 갈곳 있을때까지 돌면서
구역 수 더해주는 방법
"""
import sys
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

input = sys.stdin.readline
N,M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
area = 0

def fixed_line(point, range):
    if 0 <= point < range:
        return point
    elif point < 0:
        return (range - 1)
    else:
        return 0

def bfs(r, c):
    visited[r][c] = True
    q = deque([(r, c)])

    while (q):
        r, c= q.popleft()
        for idx in range(4):
            nr = fixed_line(r + dr[idx], N)
            nc = fixed_line(c + dc[idx], M)

            if not maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr , nc))

for r in range(N):
    for c in range(M):
        if not maps[r][c] and not visited[r][c]:
            bfs(r,c)
            area += 1
print(area)


            


