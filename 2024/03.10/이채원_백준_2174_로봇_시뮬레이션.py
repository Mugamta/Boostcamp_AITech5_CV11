import sys
#input
def solution() :
    A, B = map(int, sys.stdin.readline().split()) #col, row
    N, M = map(int, sys.stdin.readline().split()) #로봇 개수 N, 명령 개수 M
    robot = list(list(map(str, sys.stdin.readline().split())) for _ in range(N)) #각 로봇의 초기 위치
    arr = list(list(map(str, sys.stdin.readline().split())) for _ in range(M)) # M개의 명령(명령을 내리는 로봇, 명령의 종류, 명령 반복 횟수)

    for i in range(N) :
        robot[i][0]=int(robot[i][0])
        robot[i][1] = int(robot[i][1])
    for i in range(M) :
        arr[i][0] = int(arr[i][0])
        arr[i][2] = int(arr[i][2])

    move = [[0,1], [0,-1], [1,0], [-1,0]] #E, W, N, S
    d = {'E' : ['N',0,'S'], 'W' : ['S', 1, 'N'], 'N' : ['W', 2, 'E'], 'S' : ['E', 3, 'W']}

    for i in range(M) :
        r, mm, n = arr[i] #로봇, 명령 종류, 명령 반복 횟수
        
        for j in range(n) :

            c_ = robot[r-1][0] #로봇의 현재 위치
            r_ = robot[r-1][1]
            b_ = robot[r-1][2] #로봇의 현재 방향
            if mm == 'F' : #앞으로 이동하는 명령
                move_idx = d[b_][1] 
                dc = c_ + move[move_idx][1]
                dr = r_ + move[move_idx][0]

                if 0<dc<=A and 0<dr<=B : #보드 범위 안에 있다면
                    #다른 로봇과 충돌하는지 검사
                    for k,[cc, rr, _] in enumerate(robot) : 
                        if k+1 != r :
                            if dc == cc and dr == rr : 
                                return(f"Robot {r} crashes into robot {k+1}")
                            
                    robot[r-1][0] = dc #로봇 위치 바꿔주기
                    robot[r-1][1] = dr
                else : #벽과 충돌
                    return(f"Robot {r} crashes into the wall")
                    break
            elif mm == 'L' : # 왼쪽으로 방향 전환 명령
                robot[r-1][2] = d[b_][0]
            elif mm == 'R' : #오른쪽으로 방향 전환 명령
                robot[r-1][2] = d[b_][2]


    return("OK")

print(solution())
