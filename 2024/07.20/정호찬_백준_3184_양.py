"""
    메모리 : 34096 KB
    시간 : 128ms
"""
from collections import deque
import sys

iput = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x ,y):
    q = deque([(x, y)])
    t_wolf = 0
    t_sheep = 0

    if maps[x][y] == 'v':
        t_wolf += 1
    elif maps[x][y] == 'o':
        t_sheep += 1

    maps[r][c] = '#'
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = dx[idx] + x
            ny = dy[idx] + y
            if (0 <= nx < R) and (0 <= ny < C) and maps[nx][ny] != '#':
                if (maps[nx][ny]) == 'v':
                    t_wolf += 1
                elif (maps[nx][ny]) == 'o':
                    t_sheep += 1
                maps[nx][ny] = '#'
                q.append((nx, ny))

    if (t_sheep > t_wolf):
        return ('s', t_sheep)
    return ('w', t_wolf)

R, C = map(int, input().split())
maps = [[f for f in input().strip()] for _ in range(R)]

sheep, wolf = 0, 0

for r in range(R):
    for c in range(C):
        if (maps[r][c] != '#'):
            win, num = bfs(r, c)
            if (win == 's'):
                sheep += num
            else:
                wolf += num

print(sheep, wolf)