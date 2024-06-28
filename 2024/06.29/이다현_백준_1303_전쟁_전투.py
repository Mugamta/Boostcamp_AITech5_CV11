import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1,1,0,0],[0,0,-1,1]
m,n = map(int, input().split())
maps = []
w,b = 0,0 #WB점수
for _ in range(n):
    maps.append(list(input().strip()))

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    state = maps[x][y]
    maps[x][y] = '0' #방문처리
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == state:
                q.append((nx,ny))
                maps[nx][ny] = '0' #방문처리
                cnt += 1
    return cnt, state

for i in range(n):
    for j in range(m):
        if maps[i][j] != '0':
            cnt, state = bfs(i,j)
            if state == "W":
                w += cnt**2
            else:
                b += cnt**2

print(w,b)
