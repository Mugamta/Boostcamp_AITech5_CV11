import sys
from collections import deque
input = sys.stdin.readline

maps = []
dx, dy = [-1,1,0,0], [0,0,-1,1] #상하좌우
for i in range(12):
  maps.append(list(input().rstrip()))

def down():
  for y in range(6):
      for x in range(10, -1, -1):
          for k in range(11, x, -1):
              if maps[x][y] != "." and maps[k][y] == ".":
                  maps[k][y] = maps[x][y]
                  maps[x][y] = "."
                  break

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = 1 #방문처리
  cnt_tmp = deque()
  cnt_tmp.append((x,y))
  
  while q:
    x,y = q.popleft()
    tmp = maps[x][y] #해당 칸의 뿌요 색

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<12 and 0<=ny<6 and maps[nx][ny] == tmp and not visited[nx][ny]: #맵 안이며 색이 같고 방문하지 않았을 때

        q.append((nx,ny))
        cnt_tmp.append((nx,ny))
        visited[nx][ny] = 1
  return cnt_tmp



ans = 0
while True:
  flag = 0
  visited = [[0]*6 for _ in range(12)]

  for i in range(11,-1,-1):
      for j in range(6):
          if maps[i][j] != '.' and not visited[i][j]:
          
            visited[i][j] = 1
            cnt_tmp = bfs(i, j)
            if len(cnt_tmp) >= 4 :
              flag = 1
              for x,y in cnt_tmp:
                maps[x][y] = "."
            
  if flag == 0: #전체를 탐색해도 없다면
    break
  down() #다운
  ans += 1

print(ans)


