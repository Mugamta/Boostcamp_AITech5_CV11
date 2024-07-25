"""
    메모리 : 34088 KB
    시  간 : 276 MS
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    paint_ragne = 1
    maps[x][y] = 0
    q = deque([(x, y)])
    while (q):
        x, y = q.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y

            if (0 <= nx < n and 0 <= ny < m and maps[nx][ny]):
                maps[nx][ny] = 0
                paint_ragne += 1
                q.append((nx, ny))
    return (paint_ragne)

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

count = 0
max_paint_range = 0

for i in range(n):
    for j in range(m):
        if maps[i][j]:
            count += 1
            max_paint_range = max(bfs(i, j), max_paint_range)

print(count)
print(max_paint_range)
