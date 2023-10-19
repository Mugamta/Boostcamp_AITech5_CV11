import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
year = 0
one = True
S = [[0,-1], [0,1], [-1,0], [1,0]] #4가지 인접 방향

def isone(arr) : #빙하가 한 덩어리인지 검사
    d = deque()
    visited = list(list(False for _ in range(M)) for _ in range(M))
    start_temp = False
    #시작 지점 데큐에 집어넣기
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] != 0 and visited[i][j] == False:
                d.append([i,j])
                visited[i][j] = True
                start_temp = True
                break
        if start_temp :
            break
    #시작 지점부터 한 덩어리인 빙하 visit
    while d :
        # print(f"d : {d}")
        row, col = d.popleft()
        #상하좌우 검사
        for s in range(4) :
            nr = row + S[s][0]
            nc = col + S[s][1]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]!=0 and visited[nr][nc]== False :
                d.append([nr,nc])
                visited[nr][nc]=True

    #또 다른 덩어리의 빙하가 존재하는지 검사
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] != 0 and visited[i][j] == False:
                return False
    return True

def iszero(arr) : #빙하가 전부 녹았는지 검사
    s = 0
    for i in range(N) :
        s += sum(arr[i])
    if s==0 : return True
    else : return False

temp_arr = list( list( 0 for _ in range(M)) for _ in range(N))

one = isone(arr)

while one :
    #빙하가 전부 녹았는지 검사 
    if iszero(arr) :
        break
    year += 1
    for row in range(N) :
        for col in range(M) :    
            if arr[row][col] != 0 : #빙하일 경우 
                #동서남북 중 바다가 얼마나 있는지 검사
                sea = 0
                for s in range(4) :
                    nr = row + S[s][0]
                    nc = col + S[s][1]
                    if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0 :
                        sea += 1

                #인접한 바다 칸 개수만큼 빙하 녹음
                temp_arr[row][col] = max(0, arr[row][col]-sea)
    
    arr = temp_arr #array upadate
    # print(f"year:{year}, arr : {arr}")

    #빙하가 나뉘어졌는지 검사
    one = isone(arr)

if one == True : print("0")
else : print(str(year))

