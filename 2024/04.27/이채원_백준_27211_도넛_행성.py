import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
district  = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
visited = list(list(False for _ in range(M)) for _ in range(N))
move = [[1,0],[0,1],[-1,0],[0,-1]] #상하좌우 이동

num = 0  #구역 개수


#dfs
for r in range(N) : 
    for c in range(M) :
        if district[r][c] == 0 and visited[r][c] == False : 
            d = deque() 
            d.append([r,c]) #순회 시작 점의 좌표
            num += 1 #새로운 구역 number
            visited[r][c] = True
            district[r][c] = num 

            while d :
                row, col = d.popleft()

                for m in range(4) : #상하좌우 검사
                    r_new = (row + move[m][0]) % N
                    c_new = (col + move[m][1]) % M
                    if district[r_new][c_new] == 0 and visited[r_new][c_new] == False : 
                        district[r_new][c_new] = num
                        visited[r_new][c_new] = True
                        d.append([r_new,c_new])

print(num)






