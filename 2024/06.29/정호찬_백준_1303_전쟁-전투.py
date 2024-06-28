"""
    메모리 : 34088 KB
    시  간 : 72 ms
"""

import sys
from collections import deque

input = sys.stdin.readline
s_dict = {'W' : 0, 'B' : 0} #스코어 저장 
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y): #bfs와 재귀로 영역 게산
    score = 1
    vis[x][y] = 1
    q = deque([(x, y)])
    while (q):
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < M and 0 <= ny < N and vis[nx][ny] == 0 and maps[x][y] == maps[nx][ny]:
                score += bfs(nx, ny)
    return (score)

N, M = map(int, input().split())
maps = [list(input().strip()) for _ in range(M)]
vis = [[0]*(N) for _ in range(M)]

for x in range(M):
    for y in range(N):
        if vis[x][y] == 0:
            s_dict[maps[x][y]] += (bfs(x, y))**2 # 반환 받은 영역의 제곱을 더해줌

#W, B 스코어 출력
print(*s_dict.values())
