'''
메모리 : 34132KB
시간 : 2036ms
'''

from collections import deque
import copy

def get_safearea(board, N, M):
    
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    queue = deque()
    VIRUS_AREA = 0 
    SAFE_AREA =0
    
    for row in range(N):
        for col in range(M):
            
            if board[row][col]==0:
                SAFE_AREA += 1 
            
            if board[row][col]==2:
                queue.append([row, col])

    ## 바이러스가 있는 좌표가 queue에서 사라질때까지 바이러스 확산 범위를 구하기
    
    while queue:
        
        row, col = queue.popleft()
        
        for dr, dc in dirs:
            
            cr, cc= row+dr, col+dc
            
            if not (0<=cr<N and 0<=cc<M):
                continue
            
            if board[cr][cc]==0:
                queue.append([cr, cc])
                board[cr][cc] = 2
                VIRUS_AREA += 1        
    
    return SAFE_AREA - VIRUS_AREA
    
    

def main():
    
    N, M = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    MAX_AREA = 0
    
    ## 벽이 될 수 있는 3개의 좌표 선택
    for p1 in range(N*M):
        
        row1, col1 = p1//M, p1%M
        
        if board[row1][col1]:
            continue
        
        for p2 in range(p1+1, N*M):
            
            row2, col2 = p2//M, p2%M
            
            if board[row2][col2]:
                continue
            
            for p3 in range(p2+1, N*M):
                
                row3, col3 = p3//M, p3%M
                
                if board[row3][col3]:
                    continue

                ## 벽을 new_board에 설정 
                new_board = copy.deepcopy(board)
                new_board[row1][col1] = 1
                new_board[row2][col2] = 1
                new_board[row3][col3] = 1

                ## new_board의 안전영역의 크기를 구하고, 최대 크기를 업데이트
                MAX_AREA = max(MAX_AREA, get_safearea(new_board,N,M))      
        
    print(MAX_AREA)

    
if __name__ =='__main__':
    main()