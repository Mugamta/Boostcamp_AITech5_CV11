'''
12:55

조건을 만족하는 국경선 열린 곳을 bfs로 탐색(4개의 방향)
bfs를 통해 하나로 묶이는 셀들의 합(열린 국경 국가들) / 개수  -> 평균

모든 위치를 방문하며 열린 국경의 평균을 모두 구하였을때,
횟수를 증가시키고, 국경이 열리지 않을때까지 반복


01:35
visited 배열에서 방문처리 오류 발견(다른 열이 함께 True로 처리하는 현상)

02:10
완료

'''

from collections import deque

def main():
    
    N, L, R = map(int, input().split(' '))
    mat =[]
    
    for i in range(N):
        mat.append(list(map(int, input().split(' '))))
        
    time =0
    
    
    while True:
        
        # visited = [[False]*N]*N    ## 방문처리 오류 발생
        visited = [[False for i in range(N)] for t in range(N)]
        opened =0       ## 국경 개방 여부(종료조건)
        
        for row in range(N):
            for col in range(N):
                
                if visited[row][col]==False:   ## 방문하지 않았다면
                    
                    index_list =[]
                    index_list.append([row,col])
        
                    visited[row][col]= True                    
                    total_sum = mat[row][col]
                    total_cell = 1
                    
                    queue = deque([[row,col]])

                    
                    while queue:        ## BFS
                        
                        r,c = queue.popleft()
                
                        for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
                            
                            moved_r, moved_c = r+dir[0], c+dir[1]
                            
                            if moved_r <0 or moved_r>=N or moved_c<0 or moved_c>=N: ## 범위 이탈 case
                                continue
                            elif visited[moved_r][moved_c]:         ## 이미 방문한 경우
                                continue
                            
                            elif L<= abs(mat[r][c]-mat[moved_r][moved_c]) <=R:      ## 국경 개방 조건 만족
                                queue.append([moved_r, moved_c])    ## bfs
                                visited[moved_r][moved_c]= True     ## 방문 처리
                                index_list.append([moved_r, moved_c])
                                
                                total_sum += mat[moved_r][moved_c]
                                
                                total_cell += 1     ## 개방된 국경으로 묶이는 그리드의 수 update
                                opened +=1          ## 국경 개방 여부

                    
                for index in index_list:        ## 개방된 셀들을 평균으로
                    y, x = index
                    mat[y][x]= int(total_sum/total_cell)

                else:
                    continue
                
        if not opened:  ## 국경개방이 되지 않은 경우 종료
            break
        else:
            time+=1     ## 국경개방이 된 경우 다시 while loop
                        
    print(time)  
           
main()
