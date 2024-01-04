#백준 n16234 인구이동 골드5

# 11:40 시작 NxN 의 맨 처음부터 검사-> c라는 deque에 인접 국가 4개를 expand해가면서 조건에 맞으면 pop해서 연합 리스트에 넣고 안맞으면 다시 append 해보자...
# 11:50 : 검사완료조건을 잘못 생각해서 무한루프 
#12:36 자꾸 무한루프
#1:13 : visited 고치고 무한루프 해결했으나 예제 4,5 오류 => moved 를 잘못 쓴거였음
#1:20 : 제출=>통과


import sys
from collections import deque
# from collections import defaultdict

def movepple() :
    day = 0
    move = [[-1,0],[0,-1],[0,1],[1,0],]
    N, L, R = map(int, sys.stdin.readline().split())
    A = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))   
    flag = True
    visited = [[False for _ in range(N)] for _ in range(N)]
    while flag == True : 
        
        flag = False 
        for i in range(N) :
            for j in range(N) :
                # print("(i,j) :",i,j)
                if visited[i][j] == False : #한 점에 대해 
                    # print("visit")
                    visited[i][j] = True
                    union =[[i,j]]
                    d = deque()
                    d.append([i,j])
                    while d :   #연합찾기 
                        row, col = d.popleft()
                        for k in range(4) : 
                            nr, nc = row + move[k][0], col + move[k][1]
                            if nr>=0 and nc>=0 and nr<N and nc<N and visited[nr][nc] == False :
                                pp = abs(A[row][col] - A[nr][nc])
                                if pp >= L and pp<= R :
                                    d.append([nr,nc])
                                    visited[nr][nc] = True
                                    union.append([nr,nc])
                    # print("union : ",union)
                    #한 연합 다 찾았으면 인구 이동
                    if len(union)>1 :                                                 
                        p= sum(list(A[x][y] for x,y in union))//len(union)
                        flag = True # 연합이 존재함. 
                        for r,c in union :                            
                            A[r][c] = p   
                        # print("changed A : ",A)                        
        if flag :
            day+=1  
            # print("day : ",day)         
            visited = [[False for _ in range(N)] for _ in range(N)]
        else : break
    print(day)
movepple()