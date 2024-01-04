#1:19 시작
#출발지점에서 종료 지점까지 "가장 빠른 거리!"
#특별이동방법 횟수가 정해져 있다는 점에서 예전에 풀었던 말이 되고픈 원숭이 문제 생각이 남
#동일한 방법으로 BFS, visited 배열 구성
#1:50 예제 통과 후 첫 제출

import sys
from collections import deque
move = [(0,-1),(0,1),(-1,0),(1,0)] #좌 우 상 하 
def escape() :
    answer = 0
    N, M = map(int, sys.stdin.readline().split()) #미로 크기
    Hx, Hy = map(int, sys.stdin.readline().split()) #현재 위치
    Hx-= 1
    Hy-=1
    Ex, Ey = map(int, sys.stdin.readline().split()) #탈출 위치
    Ex-=1
    Ey-=1
    wall = list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) #벽 정보
    #지팡이 사용 여부까지 총 3차원의 visited 배열
    visited= list(list(list(False for _ in range(M)) for _ in range(N)) for _ in range(2))
   

    d = deque() #현재 x, 현재 y, 이동 횟수, 지팡이 사용 횟수
    d.append([Hx, Hy, 0, 1])

    while d : 
        r, c, m, w = d.popleft()

        if r==Ex and c==Ey : #Target node라면
            return m
        else : #Target이 아니라면 expand
            for i in range(4) : 
                new_r = r + move[i][0]
                new_c = c + move[i][1]
                if (0 <= new_r < N) and (0 <= new_c < M) and wall[new_r][new_c] == 0 :
                    #보드 내 범위이고 벽이 없다면 expand
                    if visited[w][new_r][new_c] == False :
                        visited[w][new_r][new_c] = True 
                        d.append([new_r, new_c, m+1, w])
                elif (0 <= new_r < N) and (0 <= new_c < M) and wall[new_r][new_c] == 1 :
                    #보드 내 범위이지만 벽이 있다면 
                    if w == 1 : #지팡이 쓸 수 있다면
                        visited[0][new_r][new_c] = True
                        d.append([new_r, new_c, m+1, 0])
                    else : #지팡이 쓸 수 없다면 
                        continue
                else : #보드 범위 벗어난다면 
                    continue
    return -1
print(escape())

        



