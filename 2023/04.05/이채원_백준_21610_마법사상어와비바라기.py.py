#백준 마법사 상어와 비바라기 골드5
#10:30 start ==> 그냥 읽으면서 써있는대로 구현하는 문제 같았음
#11:10 예제 테스트 -> 틀림 -> M 번 이동시 구름이 계속 맨 처음 자리로 리셋되는줄 착각해서( 문제를 잘 읽자! )
#11:28 예제 다 맞아서 첫 제출 -> 바로 시간초과
#  전에 구름이 떴던 자리인지 찾는걸 cloud array에 좌표가 들어있는지 여부로 (매번 cloud 순회 ) 찾지 않고 visited 배열을 만들어 복잡도 줄임
#11:43 재제출 -> 통과

import sys

def shark() :
    N, M = map(int, sys.stdin.readline().split())
    arrN = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    arrM = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))

    answer = 0
    dir = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]] #direction
    v = [[-1,-1],[-1,1],[1,-1],[1,1]] #대각선

    cloud = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]
    cl = [[False for _ in range(N)] for _ in range(N)] 

    for d, s in arrM : # M 번 구름을 이동시키기
        d = d-1
        dr = dir[d][0] * s
        dc = dir[d][1] * s
        for j in range(len(cloud)) :
            row, col = cloud[j]
            row += dr
            col += dc
            if row < 0 : 
                row = row  + ((-1*row)//N + 1)*N 
            if col < 0 : 
                col = col + ((-1*col)//N + 1)*N
            if row > N-1 : 
                row = row % N
            if col > N-1 : 
                col = col % N 
          
            cloud[j] = [row,col]
            arrN[row][col] += 1 #구름이 있는 곳 물 1 증가
            cl[row][col] = True  #구름이 있던 자리 백업
        
        for j in range(len(cloud)) : #물복사버그 
            row, col = cloud[j]
            for k in range(4) : #대각선 검사
                tr = row + v[k][0]
                tc = col + v[k][1]
                if tr >= 0 and tr < N and tc >= 0 and tc < N and arrN[tr][tc] > 0 : 
                    arrN[row][col] += 1        
        cloud = []
        for i in range(N) :  #5번 구현
            for j in range(N) :
                if arrN[i][j] >= 2 :
                    if cl[i][j] == False :
                        arrN[i][j]-=2
                        cloud.append([i,j])  
                    
                cl[i][j ]= False
    return sum(list(sum(arrN[i]) for i in range(N)))


print(shark())
