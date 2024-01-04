def solution(grid):
    result = []     ## loop 길이 저장할 리스트
    visited = [[[False for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(4)]      ## N x N nodes, 4 방향
    
    ways, rows, cols = 4, len(grid), len(grid[0])
    
    for way in range(ways):         ## 4개의 방향에 대해
        for row in range(rows):     ## 모든 행열 위치에 대해
            for col in range(cols):
                if visited[way][row][col]:      ## 이미 탐색한 경로의 경우 다음을 탐색
                    continue
                else:                           ## 탐색하지 않은 경로
                    w, r, c = way, row, col
                    num =0                      ## 사이클의 길이를 측정할 변수 num
                    
                    while True:                 ## 지점으로부터 가능한 경로 반복적 탐색
                        if visited[w][r][c]:    ## 방문한 경로이면 
                            break
                        
                        num+=1                  ## 사이클 길이를 +1
                        visited[w][r][c]= True  ## 경로 방문 처리
                        
                        ## 방향에 따른 이동 구현 ##
                        if w==0:        ## right
                            if grid[r][c]=='S':
                                c = (c+1)%cols
                            elif grid[r][c]=='R':
                                r = (r+1)%rows
                                w = 1
                            else:
                                r = (r-1)%rows
                                w = 3
                        elif w==1:      ## down
                            if grid[r][c]=='S':
                                r = (r+1)%rows
                            elif grid[r][c]=='R':
                                c = (c-1)%cols
                                w = 2
                            else:
                                c = (c+1)%cols
                                w = 0
                        elif w==2:          ## left
                            if grid[r][c]=='S':
                                c = (c-1)%cols
                            elif grid[r][c]=='R':
                                r = (r-1)%rows
                                w = 3
                            else:
                                r = (r+1)%rows
                                w = 1
                        else:               ## up
                            if grid[r][c]=='S':
                                r = (r-1)%rows
                            elif grid[r][c]=='R':
                                c = (c+1)%cols
                                w = 0
                            else:
                                c = (c-1)%cols
                                w = 2

                    result.append(num)
                        
    return sorted(result)