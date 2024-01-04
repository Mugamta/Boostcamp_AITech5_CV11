def main():
    
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append([i for i in input()])
    
    while N>=2:     ## 크기 N부터 2가 될때까지 matrix를 줄여나감
        new_mat =[]
        
        for row in range(0,N,2):    ## stride 2
            line = []
            
            for col in range(0,N,2):    ## stride 2
                target = [mat[row][col],mat[row][col+1],mat[row+1][col],mat[row+1][col+1]]      ## 탐색 대상
                if all(i=='1' for i in target):         ## 탐색 대상이 모두 1인 경우 1로
                    line.append('1')
                elif all(i=='0' for i in target):       ## 탐색 대상이 모두 0인 경우 0으로
                    line.append('0')
                else:
                    line.append('('+''.join(target) +')')   ## 탐색 대상이 여러개가 섞여있는 경우, 그대로 유지하고 괄호 적용
            
            new_mat.append(line)
        
        mat = new_mat
            
        N //= 2
     
    print(mat[0][0])
    
main()
