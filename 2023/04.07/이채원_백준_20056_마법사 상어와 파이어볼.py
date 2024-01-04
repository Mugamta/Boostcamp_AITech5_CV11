#12:30 시작 ==> 구현/시뮬레이션
#1:39 예제 통과=> 첫 제출
import sys

def shark() :
    
    N, M, K = map(int, sys.stdin.readline().split())
    arrN = [[[] for _ in range(N)] for _ in range(N)] #NxN
    arrM = list(list(map(int, sys.stdin.readline().split())) for _ in range(M)) #파이어볼
    dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    

    for m in range(K) : #K번 이동
        #1
        for r, c, m, s, d in arrM : #M개의 파이어볼 이동
            nr = r + dir[d][0]*s
            nc = c + dir[d][1]*s
            nr = nr % N
            nc = nc % N
            if nr < 0 : nr += N
            if nc < 0 : nc += N
            
            arrN[nr][nc].append([m,s,d])

        # 2
        arrM = []
        for i in range(N) :
            for j in range(N) :
                if len(arrN[i][j]) > 1 : #두개 이상일 경우
                    m = sum(list(x[0] for x in arrN[i][j]))//5 #질량
                    if m > 0 :
                        s = sum(list(x[1] for x in arrN[i][j]))//len(arrN[i][j]) #속력
                        d = sum(list(x[2]%2 for x in arrN[i][j]))
                        if d == 0 or d == len(arrN[i][j]) : #모두 짝수거나 모두 홀수일 경우 
                            d = [0,2,4,6]
                        else : d = [1,3,5,7]
                        for dd in d :
                            arrM.append([i,j,m,s,dd])
                        
                elif len(arrN[i][j]) == 1 : #한개일 경우 
                    # print(arrN[i][j])
                    m,s,d = arrN[i][j][0]
                    arrM.append([i,j,m,s,d])
                arrN[i][j]=[]
                    
    return sum(list(x[2] for x in arrM))

print(shark())

