import sys

def clean() :
    #입력 받기
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    wall = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    clean = [[False for _ in range(M)] for _ in range(N)]
    robot = [[0,-1], [1,0], [0,1], [-1,0]] #북동남서 
    while(True) :

        clean[r][c] = True #현재 칸 청소 체크       
        tmp = 0

        for i in range(4) : #현재 주위 4칸 검사
            nr = r + robot[i][1]
            nc = c + robot[i][0]
            if nc>=0 and nr >= 0 and  nr < N and nc < M :
                if wall[nr][nc] == 0 and clean[nr][nc]==0 : #청소되지 않은 빈칸이 있는지 
                    tmp = 1
                    break
                    
        if tmp == 0 : #청소되지 않은 빈 칸이 없는 경우 
            nr = r - robot[d][1]
            nc = c - robot[d][0]

            if nc >= 0 and nr >= 0 and  nr < N and nc < M :
                if wall[nr][nc]==0 : #후진할 수 있다면 후진
                    r = nr
                    c = nc
                else : #후진 불가능1 : 벽있음 -> 종료
                    answer = 0
                    for i in range(N) :
                        answer += clean[i].count(True)
                    return answer 
            else : #후진 불가능2 : 보드 범위 벗어남 -> 종료
                answer = 0
                for i in range(N) :
                    answer += clean[i].count(True)
                return answer 
            
        else : #청소되지 않은 빈 칸이 있는 경우 (tmp = 1)
            if d>0 : d -=1 
            else : d = 3  #반시계 방향 회전
            nr = r + robot[d][1] 
            nc = c + robot[d][0]
            #전진조건 확인
            if nr >= 0 and nc >= 0 and  nr < N and nc < M : #보드 범위 안이고
                if wall[nr][nc] == 0 and clean[nr][nc]==0 : #벽이 없고 청소되지 않았을 경우 
                    r = nr
                    c = nc
print(clean())