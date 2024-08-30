import copy
from collections import deque
n = int(input()) #보드 크기
k = int(input()) #사과 개수
maps = [[0]*n for _ in range(n)]
dx,dy = [-1,0,1,0],[0,1,0,-1] #북동남서
for _ in range(k):
    x,y = map(int, input().split())
    maps[x-1][y-1] = 1 #사과 넣어주기

dic = {} #방향정보
l = int(input()) #방향 수
for _ in range(l):
    x, c = map(str, input().split())
    dic[int(x)] = c

d = 1 #처음엔 오른쪽을 향함
x,y = 0,0 #첫 시작 좌표
q =deque()
q.append((x,y)) #뱀
maps[x][y] = -1
cnt = 0
while q:
    nx,ny = x+dx[d], y+dy[d] #이동
    if 0<=nx<n and 0<=ny<n: # 이동한 칸이 맵 안이라면
        cnt += 1
        if maps[nx][ny] == 0 : #빈칸일 경우
            sx, sy = q.popleft()  # 뱀의 꼬리 없애줌
            maps[sx][sy] = 0  #뱀의 꼬리 없애줌
            maps[nx][ny] = -1 #뱀 이동
            q.append((nx, ny))
            x,y = nx,ny
        elif maps[nx][ny] == 1: #사과일 경우 (꼬리 유지)
            maps[nx][ny] = -1 #뱀 이동
            q.append((nx,ny))
            x,y = nx,ny
        else : #맵 안에는 있는데 뱀 자신을 만나거나 벽에 부딪힌 경우
            break #바로 종료
        if cnt in dic: #방향 변환이 필요한 경우
            if dic[cnt] == 'D':
                d = (d+1)%4
            else :
                d = (d-1)%4
    else :
         cnt+=1
         break
    

print(cnt)
