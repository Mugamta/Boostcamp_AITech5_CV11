'''
메모리 : 31120KB
시간 : 48ms
'''

def main():
    
    
    N, M = map(int, input().split())
    
    board = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for _ in range(M):
        board.append([i for i in input()])
    
    visited = [[False for _ in range(N)] for _ in range(M)]
    
    w,b = 0,0
    
    ## 모든 좌표에 대하여
    for r in range(M):
        for c in range(N):
            
            ## 방문하지 않은 좌표인 경우
            if not visited[r][c]:
                
                ## queue에 넣고 방문 표시
                queue = [[r,c]]
                target = board[r][c]
                total = 0
                
                ## queue의 좌표들을 방문
                for row, col in queue:
                    
                    ## 4방향에 대해 탐색, 범위 내이고 방문하지 않은 좌표인 경우
                    for dr, dc in dirs:
                        if (0<=row+dr<M) and (0<=col+dc<N) and not visited[row+dr][col+dc]:
                            
                            ## 좌표에 같은 국적의 병사가 있는 경우, 다음 탐색을 위해 추가
                            if target==board[row+dr][col+dc]:
                                total +=1
                                queue.append([row+dr, col+dc])
                                visited[row+dr][col+dc]=True
                
                if total==0:
                    if target=='W':
                        w+=1
                    else:
                        b+=1
                else:
                    if target=='W':
                        w+=total**2
                    else:
                        b+=total**2

    print(w,b)
    return 0


if __name__ == '__main__':
    main()