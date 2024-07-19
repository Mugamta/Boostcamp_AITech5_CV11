from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int, input().split())
dx, dy = [-1,1,0,0], [0,0,-1,1]
maps = []
# . 빈 필드, # 울타리, o 양, v 늑대
for i in range(r):
    maps.append(list(input().rstrip()))


def bfs(x,y,maps):
    o,v = 0,0 #양 늑대 수
    q = deque()
    q.append((x,y))
    if maps[x][y]=='o' :
        o+=1
    elif maps[x][y]=='v' :
        v+=1
    maps[x][y] = '#' #방문처리
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny] != '#':
                if maps[nx][ny] == 'o':
                    o += 1
                elif maps[nx][ny] == 'v':
                    v += 1
                maps[nx][ny] = '#' #방문처리
                q.append((nx,ny))
    return o,v

res_o,res_v = 0,0
for i in range(r):
    for j in range(c):
        if maps[i][j] != '#': #울타리가 아니라면
            o,v = bfs(i,j,maps)
            if o>v: #양이 더 많으면
                res_o += o
            else :
                res_v += v
print(res_o, res_v)

