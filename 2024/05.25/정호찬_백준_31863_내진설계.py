import sys
from collections import deque
input = sys.stdin.readline

x_y = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N,M = map(int, input().split())
vis = [[0]* M for _ in range(N)] #방문
maps = [list(map(str, input())) for _ in range(N)]

building, destroy= 0, 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == '@':
            start = (i, j)
        elif maps[i][j] == '#' or maps[i][j] == '*':
            building += 1

q = deque()
# 진원지의 지진 시뮬
 # 2칸 까지 영향을 줌으로
for dx, dy in x_y:
    for idx in range(2):
        nx = start[0] + dx * (idx + 1)
        ny = start[1] + dy * (idx + 1)

        #멈춤 조건
        if (nx < 0 or nx >= N or ny < 0 or ny >= M  or maps[nx][ny] == '|'):
            break
        if (maps[nx][ny] == '.'):
            continue

        #내진 설계된 건물이라면-> 내진 설계 안된 건물로 변경
        if (maps[nx][ny] == '#'):
            maps[nx][ny] = '*'
        elif (maps[nx][ny] == '*'):
            vis[nx][ny] = 1 # 방문처리하고 
            q.append((nx, ny)) # 무너질 건물에 추가

#이제 무너질 건물의 여진을 시뮬
while q:
    x, y = q.popleft()
    #무너짐 처리
    maps[x][y] = '.'
    destroy += 1
    for dx, dy in x_y:
        nx = x + dx
        ny = y + dy

        #멈춤 조건
        if (nx < 0 or nx >= N or ny < 0 or ny >= M  or maps[nx][ny] == '|' or maps[nx][ny] == '.'):
            continue

        #내진 설계된 건물이라면-> 내진 설계 안된 건물로 변경
        if (maps[nx][ny] == '#'):
            maps[nx][ny] = '*'
        #방문안한 내진 설계가 안된 건물이라면 
        elif (maps[nx][ny] == '*' and vis[nx][ny] == 0):
            vis[nx][ny] = 1
            q.append((nx, ny))

print(destroy, building - destroy)
