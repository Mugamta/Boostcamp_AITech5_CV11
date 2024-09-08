import copy

def diffusion(room, room_dif, R, C):
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for r in range(R):
        for c in range(C):
            
            if room[r][c]==-1:
                continue
            
            dust = room[r][c]//5
            
            for dr, dc in dirs:
                
                if 0<=r+dr<R and 0<=c+dc<C:
                    if room[r+dr][c+dc]==-1:
                        continue
                    
                    room_dif[r+dr][c+dc] += dust
                    room[r][c] -= dust
    
    for r in range(R):
        for c in range(C):
            if room[r][c]==-1:
                continue
            
            room[r][c] += room_dif[r][c]
    
    return room
                    
                    
def move(room,rr ,cc,R, C, TOTAL):
    ### 위
    TOTAL -= room[rr-2][cc]   
    
    for i in range(rr-2,0,-1):
        room[i][cc]= room[i-1][cc]
    
    for i in range(0, C-1):
        room[0][i] = room[0][i+1]
    
    for i in range(0,rr-1):
        room[i][C-1] = room[i+1][C-1]
    
    for i in range(C-1, 1,-1):
        room[rr-1][i] = room[rr-1][i-1]
        
    room[rr-1][1] = 0
    
    
    ## 아래
    TOTAL -= room[rr+1][cc]
    
    for i in range(rr+1, R-1):
        room[i][cc] = room[i+1][cc]
    
    for i in range(0, C-1):
        room[R-1][i] = room[R-1][i+1]
    
    for i in range(R-1, rr, -1):
        room[i][C-1] = room[i-1][C-1]
    
    for i in range(C-1, 1, -1):
        room[rr][i] = room[rr][i-1]
    
    room[rr][1]=0

    return room, TOTAL

def main():
    
    R, C, T = map(int, input().split())
    TOTAL = 0
    
    room = [list(map(int, input().split())) for _ in range(R)]
    room_dif = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if room[r][c]==-1:
                ## 공기청정기 좌표
                rr, cc = r ,c
                continue
            
            TOTAL += room[r][c]

    for _ in range(T):
        room = diffusion(room, copy.deepcopy(room_dif), R, C)
        room, TOTAL = move(room, rr, cc, R,C,TOTAL)
        
    print(TOTAL)
    
if __name__=="__main__":
    main()