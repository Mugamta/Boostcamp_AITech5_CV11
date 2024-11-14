"""
메모리 : 34072KB
시간 : 196ms
"""
from collections import deque

def main():
    N, M = map(int,input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    ## 탐색할 지점들을 담을 queue
    queue = deque()
    queue.append((0,0))
    
    ## 방문 여부를 체크하면서, 해당 지점으로 갈 수 있는 최소 횟수를 저장(dp)
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = 0
    
    while queue:
        r,c = queue.popleft()
        ## booster : 해당 지점에서 이동 가능한 최대 거리
        booster = board[r][c]
        
        ## 종료 지점 도착시
        if r==N-1 and c==M-1:
            print(visited[r][c])
            return 0
        
        ## 행 방향으로 부스터 사용가능한 범위까지 queue에 추가
        for nr in range(r+1 ,min(N, r+booster+1)):
            if not visited[nr][c]:
                queue.append((nr, c))
                visited[nr][c] = visited[r][c]+1
        
        ## 열 방향으로 부스터 사용가능한 범위까지 queue에 추가
        for nc in range(c+1,min(M, c+booster+1)):
            if not visited[r][nc]:
                queue.append((r, nc))
                visited[r][nc] = visited[r][c]+1

if __name__ == '__main__':
    main()
