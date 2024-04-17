from collections import deque

def main():
    
    R, C = map(int, input().split())
    
    board = []
    water = [[False for _ in range(C)] for _ in range(R)]
    rock = [[False for _ in range(C)] for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        row = [t for t in input()]
        board.append(row)
    
    loc_queue = deque()
    water_queue = deque()
    
    ## 입력에 따라 물, 돌, 시작지점, 종료지점을 설정
    for r in range(R):
        for c in range(C):
            
            target = board[r][c]
            
            if target=='S':
                loc_queue.append([r,c])
                visited[r][c] = True
            elif target =='D':
                rr, cc = r,c
            elif target =='*':
                water[r][c] = True
                water_queue.append([r,c])
            elif target=='X':
                rock[r][c]= True
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    N =0 
    
    ## 더 이상 움직일 수 있는 위치가 없을때까지 반복
    while loc_queue:
        
        ## 물의 확장
        for _ in range(len(water_queue)):
            
            r, c = water_queue.popleft()
            ## 물이 확장되는 지점이 범위 내이고, 돌이 없고, 종료 지점이 아니고, 이미 물이 차있지 않은 경우. 확장될 지점으로 추가
            for dr, dc in dirs:
                if (0<=r+dr<R) and (0<=c+dc<C) and not rock[r+dr][c+dc] and not (r+dr==rr and c+dc==cc) and not water[r+dr][c+dc]:
                    water_queue.append([r+dr, c+dc])
                    water[r+dr][c+dc] = True            
        
    
        ## 경로의 확장
        for _ in range(len(loc_queue)):

            r, c = loc_queue.popleft()
            ## 종료 지점과 동일 시 반복횟수 반환
            if r==rr and c==cc:
                print(N)
                return 0
            
            ## 진행할 경로가 범위 내이고, 돌이 없고, 물이 없고, 방문하지 않은 지점인 경우. 이후 경로로 추가
            for dr, dc in dirs:
                if (0<=r+dr<R) and (0<=c+dc<C) and not rock[r+dr][c+dc] and not water[r+dr][c+dc] and not visited[r+dr][c+dc]:
                    loc_queue.append([r+dr, c+dc])
                    visited[r+dr][c+dc] = True      
        
        N += 1
    
    print('KAKTUS')
    return 0


if __name__ == '__main__':
    main()