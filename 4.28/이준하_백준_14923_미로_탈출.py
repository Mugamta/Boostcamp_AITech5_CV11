import sys
from collections import deque
n,m=map(int,input().split())
hx,hy=map(int,input().split())
ex,ey=map(int,input().split())
graph,visit=[],[[[0,sys.maxsize] for __ in range(m)] for _ in range(n)]
for _ in range(n):graph.append(list(map(int,input().split())))
q=deque()
q.append((hx-1,hy-1))
visit[hx-1][hy-1][1]=0
dx,dy,ans=[-1,1,0,0],[0,0,-1,1],False
while q:
    x,y=q.popleft()
    if x==ex-1 and y==ey-1 and visit[x][y][1]<=1:
        ans=True
        print(visit[x][y][0])
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<m and visit[x][y][1]<visit[nx][ny][1]:
            if graph[nx][ny]==1 and visit[x][y][1]==0:
                visit[nx][ny][0]=visit[x][y][0]+1
                visit[nx][ny][1]=1
                q.append((nx,ny))
            elif graph[nx][ny]==0 and visit[x][y][1]==1:
                visit[nx][ny][0]=visit[x][y][0]+1
                visit[nx][ny][1]=1
                q.append((nx,ny))
            elif graph[nx][ny]==0 and visit[x][y][1]==0:
                visit[nx][ny][0]=visit[x][y][0]+1
                visit[nx][ny][1]=0
                q.append((nx, ny))
if not ans:print(-1)