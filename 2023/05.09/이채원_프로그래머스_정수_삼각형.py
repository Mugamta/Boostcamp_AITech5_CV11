#12:46 시작
#더했을때 가장 큰 루트를 찾아야 함 -> 합 배열 만들기?
#어차피 바닥까진 가야함 & 가장 큰 합 -> 가능한 경우의 수 중 큰 값으로 선택해서 합 배열 만들기

def solution(triangle):
    t_sum = triangle.copy()
    for i in range(1,len(triangle)) :
        for j in range(len(triangle[i])) :
            if j == 0 :
                t_sum[i][j] = triangle[i][j] + t_sum[i-1][j]
            elif j == len(triangle[i])-1 :
                t_sum[i][j] = triangle[i][j] + t_sum[i-1][j-1]
            else :
                t_sum[i][j] = triangle[i][j] + max(t_sum[i-1][j], t_sum[i-1][j-1])
        
    
    return max(t_sum[len(triangle)-1])