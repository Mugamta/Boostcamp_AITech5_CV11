import sys
from collections import deque


#입력받기
N, M = map(int, sys.stdin.readline().split())
arr = list(list( map(int, sys.stdin.readline().split())) for _ in range(N))

move = [[-1,0], [0,1], [0,-1], [1,0]] #상하좌우
dn = deque() #도착지 destination
visited = list(list(False for _ in range(M)) for _ in range(N)) 
ans = list(list(-1 for _ in range(M)) for _ in range(N))  #-1로 초기화


for i in range(N) : # destination과 wall 찾기
    for j in range(M) :
        if arr[i][j] == 2 : #destination(목표 지점)
            dn.append([i,j])
            ans[i][j] = 0 
            visited[i][j] = True

        if arr[i][j] == 0: #원래 갈 수 없는 땅일 경우
            ans[i][j] = 0
            visited[i][j] = True

while dn :  
    r, c = dn.popleft() #row, col , 최단 거리가 탐색되도록 왼쪽에서부터 pop한다. 

    for dr, dc in move : #상하좌우 검사
        r_n = r + dr
        c_n = c + dc

        if 0 <= r_n < N and 0 <= c_n < M and visited[r_n][c_n] == False : 
            dn.append([r_n, c_n]) #상하좌우 extend
            visited[r_n][c_n] = True #방문 처리
            ans[r_n][c_n] = ans[r][c] + 1 #거리 update

#print answer
for i in range(N) :
    p = list(str(x) for x in ans[i]) 
    print(' '.join(p))

