def main():
    
    N, M = map(int, input().split())
    
    donut = [list(map(int, input().split())) for row in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt = 0
    
    for row in range(N):
        for col in range(M):
            
            target = donut[row][col]

            ## 지점이 비어있고 탐색하지 않은 지점인 경우
            ## 연결되어 있는 빈 지점(0)을 연속적으로 탐색
            if target == 0 and not visited[row][col]:
                cnt+=1
                queue =[(row,col)]
                
                while queue:
                    r, c = queue.pop()
                    
                    ## 인접한 4방향에 대해 탐색
                    for dr, dc in dirs:
                        
                        ## 나머지 연산을 활용하여 범위 이탈없이 연속된 행과 열로 표현
                        rr= (r+dr)%N
                        cc= (c+dc)%M
                        
                        ## 다음 지점이 빈 지점인 경우 
                        if donut[rr][cc]==0 and not visited[rr][cc]:
                            
                            visited[rr][cc] = True
                            queue.append((rr,cc))
    
    print(cnt)       
    return 0


if __name__ == '__main__':
    main()