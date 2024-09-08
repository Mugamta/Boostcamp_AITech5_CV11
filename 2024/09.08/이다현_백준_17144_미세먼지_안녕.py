import sys
from collections import deque
import copy
## 선언 및 입력
r,c,t = map(int,input().split()) #행, 열, Time
maps = []
dx, dy = [-1,0,1,0],[0,1,0,-1]
for i in range(r):
    maps.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c):
        if maps[i][j] == -1:
            # 공기청정기 좌표
            a,b = i,j
            break
        
def isCircle(maps): #공기청정기 바람에 의해 움직이는지
    # 2,0
    x,y = a-1,b
    idx = 1
    tmp = 0
    while 1:
        nx,ny = x+dx[idx], y+dy[idx]
        if 0<=nx<r and 0<=ny<c: # 맵 안에 있다면
            next_tmp = maps[nx][ny] #다음으로 이동해야 할 값
            maps[nx][ny] = tmp
            tmp = next_tmp
            x,y = nx,ny
        else : # 벗어난다면 방향을 바꾸기
            idx = (idx-1)%4
            continue
        if (x,y) == (a-1,b): #다 돌면
            maps[a-1][b] = -1
            break
    # 3,0
    x,y = a,b
    idx = 1
    tmp = 0
    while 1:
        nx,ny = x+dx[idx], y+dy[idx]
        if 0<=nx<r and 0<=ny<c: # 맵 안에 있다면
            next_tmp = maps[nx][ny] #다음으로 이동해야 할 값
            maps[nx][ny] = tmp
            tmp = next_tmp
            x,y = nx,ny
        else : # 벗어난다면 방향을 바꾸기
            idx = (idx+1)%4
            continue
        if (x,y) == (a,b): #다 돌면
            maps[a][b] = -1
            break


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 #방문처리
    while q:
        x,y = q.popleft()
        cnt = 0 # 확산 방향 수
        tmp = maps[x][y]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny] != -1: #맵 안에 있고 공기청정기가 아닌 경우
                cnt += 1
                if maps[nx][ny] == 0: #원래 0이었다면
                    visited[nx][ny] = 1 #방문처리
                origin_maps[nx][ny] += tmp//5
        origin_maps[x][y] += tmp-cnt*(tmp//5)


for time in range(t): #시간만큼 확산->정화
    origin_maps = [[0] * c for i in range(r)]
    visited = [[0] * c for i in range(r)]
    ## 1. 확산
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 0 and visited[i][j] == 0: # 미세먼지가 존재하며 방문하지 않았다면
                bfs(i,j)
    ## 2. 정화
    isCircle(origin_maps)
    maps = copy.deepcopy(origin_maps)

ans = 0
for i in range(r):
    ans += sum(maps[i])

print(ans+2)


