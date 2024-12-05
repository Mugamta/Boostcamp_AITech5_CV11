"""
메모리 : 40164KB
시간 : 612ms
"""
from collections import deque

def main():
    X, Y, N = map(int, input().split())
    X+= 501
    Y+= 501
    
    ## 음수 좌표 관리를 위해 배열 확장
    visited = [[False for _ in range(1002)] for _ in range(1002)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for _ in range(N):
        r, c = map(int, input().split())
        ## 확장된 배열 위한 좌표 조정
        r+= 501
        c+= 501
        visited[r][c]= True
    
    queue = deque()
    queue.append((501,501,0))
    
    while queue:
        
        r,c, distance = queue.popleft()
        
        for dr, dc in dirs:
            nr= r+dr
            nc= c+dc
            
            ## 범위 내부 확인
            if not ((0<=nr<1002) and (0<=nc<1002)):
                continue
            ## 방문 여부 확인        
            if visited[nr][nc]!= False:
                continue
            
            if nr==X and nc==Y:
                print(distance+1)
                return 0
            
            visited[nr][nc] = True
            queue.append((nr, nc, distance+1))
    
    return 0
    
if __name__ == '__main__':
    main()
