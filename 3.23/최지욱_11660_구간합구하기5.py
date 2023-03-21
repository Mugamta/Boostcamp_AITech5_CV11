'''
입력된 행렬에서 단순하게 매번 합을 구하기
-> 시간 초과(최대 M 100,000)


07:05 시작

매번 합을 구하는게 시간 초과이면 사전에 계산된
결과를 활용하는 dp를 활용하는 생각

구간이 주어졌을때 원점으로부터 4개의 각 직사각형 합을 활용하여 
직사각형 구간을 구하기

07:15

첫행과 첫열에 0으로 패딩을 주는 방법으로 구현 시작


07:30 

결과값 순서가 계속 다르게 나옴
print를 찍어보며 체크

행이 x, 열이 y라는 것을 확인

열을 y, 행을 x로 두고 풀고 있었음
->문제를 잘 읽어야

07:45 : 완료
'''

def main():
    N, num = map(int, input().split(" "))
    
    mat =[[0]*(N+1)]        ## 첫행의 zero padding
    for _ in range(N):
        row= list(map(int, input().split(" ")))
        prev = 0
        new_row =[]
        for elem in row:        ## 행의 오른쪽으로 가면서 값을 누적
            prev += elem
            new_row.append(prev)
        mat.append([0]+new_row)       ## 첫 열에 zero padding + 누적된 row
    
    for row in range(1,N+1):
        for col in range(N+1):        ## 윗 행의 누적값을 아래로 가면서 누적
            mat[row][col] = mat[row][col] +mat[row-1][col]
    
    result =[]
    for _ in range(num):
        y1,x1,y2,x2 = map(int, input().split(" "))
        
        rect_1 = mat[y1-1][x2]          ## (-), 1사분면 직사각
        rect_2 = mat[y1-1][x1-1]        ## (+), 2사분면 직사각(가장 작음)
        rect_3 = mat[y2][x1-1]          ## (-), 3사분면 직사각
        rect_4 = mat[y2][x2]            ## (+), 4사분면 직사각(전체 범위 포함, 제일 큼)
        
        result.append(rect_4-rect_1-rect_3+rect_2)  ## 구간 범위 계산
    
    for i in result:
        print(i)
      
main()