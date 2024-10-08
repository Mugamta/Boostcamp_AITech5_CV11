from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n,m = map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
maps = []
ans,max_area = 0,0 #그림 수, 그림 넓이
for i in range(n):
    maps.append(list(map(int, input().split())))

def bfs(x,y,maps):
    q = deque()
    q.append((x,y))
    maps[x][y] = 0 #방문처리
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                cnt += 1
                q.append((nx,ny))
                maps[nx][ny] = 0
    return cnt

def dfs(x,y):
    global cnt
    cnt += 1
    maps[x][y] = 0 #방문처리
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            dfs(nx,ny)
    return



for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            #max_area = max(bfs(i,j,maps), max_area)
            cnt = 0
            dfs(i,j)
            max_area = max(cnt, max_area)
            ans += 1

print(ans,max_area,sep='\n')
