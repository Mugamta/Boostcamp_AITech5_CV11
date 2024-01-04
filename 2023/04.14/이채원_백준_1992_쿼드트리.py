#백준 1992 쿼드트리
#2:35 시작 
#3:32 제출


#입력받기
N = int(input())
arr = list(list(map(int, input())) for _ in range(N))
answer = ''
#재귀함수
def quad(x, y, N) :
    global answer
    val = arr[x][y]

    #네모 영역을 검사
    #x,y부터 NxN의 영역
    for xx in range(x, x+N) :
        for yy in range(y,y+N) :
            if val != arr[xx][yy] : #값이 다르면
                #Section 시작
                answer += '('
                #왼쪽 위
                quad(xx, yy, N//2)
                #오른쪽 위
                quad(xx, yy+N//2,N//2)
                #왼쪽 아래
                quad(xx+N//2, yy, N//2)
                #오른쪽 아래
                quad(xx+N//2,yy+N//2,N//2)
                #Section 끝
                answer += ')'
                return None 
    if val == 0 : 
        answer += '0'
    elif val == 1 : 
        answer += '1'  
    




quad(0,0,N)
print(answer)
