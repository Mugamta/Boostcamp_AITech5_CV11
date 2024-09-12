'''
메모리 : 35212KB
시간 : 116ms
'''

def main():

    H,R,C = map(int,input().split())
    
    if not (H+R+C):
        return 0
    
    ## 빌딩구조 입력
    building =[]
    for h in range(H):
        
        floor =[]
        for r in range(R):
            row = input()
            
            if 'S' in row:
                ## 초기 시작 지점 정보 저장
                init = [h,r,row.index('S'), 0]
            floor.append(row)
        
        input()
        building.append(floor)
            
    ## 방문 저장을 위한 3차원 리스트
    ## height, row, column
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]
    
    dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    
    queue =[init]
    
    ## queue에 이동가능한 지점을 추가해가며 탐색(종료지점,E까지)
    for h,r,c,time in queue:
        
        for dh, dr, dc in dirs:
            
            ch, cr, cc, = h+dh, r+dr, c+dc
            
            ## 이동 가능 범위 여부
            if not (0<=ch<H and 0<=cr<R and 0<=cc<C):
                continue
            ## 비어있는 칸 여부
            if visited[ch][cr][cc] or building[ch][cr][cc]=="#":
                continue
            
            ## 종료지점인 경우 시간 출력 후 다음 케이스로
            if building[ch][cr][cc]=='E':
                print(f"Escaped in {time+1} minute(s).")
                main()
                return 0

            visited[ch][cr][cc] = True
            queue.append([ch, cr, cc, time+1])
    
    ## 이동가능 지점이 없는 경우 Trapped 후 다음 케이스로
    print("Trapped!")
    main()
    return 0

if __name__ =="__main__":
    main()
    