'''
메모리 : 41136KB
시간 : 344ms
'''
from collections import deque

def main():

    
    N,M,K = map(int, input().split())
    
    room = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    NUM =0
    
    ## 모든 위치에 대해 탐색
    for row in range(N):
        for col in range(M):
            
            ## 이미 방문한 위치인 경우
            if room[row][col]==0:
                continue

            NUM += 1
            areas = deque([(row,col)])
            
            ## 해당 위치와 연결된 모든 위치를 순회하며 탐색
            while areas:
                
                r,c = areas.pop()

                ## 이미 방문한 경우
                if room[r][c]==0:
                    continue
                    
                height = room[r][c]
                
                ## 방문 처리
                room[r][c] =0 
                
                
                ## 인접 위치 추가
                for dr, dc in dirs:
                    
                    cr, cc= r+dr, c+dc

                    
                    if not (0<=cr<N and 0<=cc<M):   ## 범위 내 여부
                        continue
                    if room[cr][cc]==0:             ## 방문 여부
                        continue
                    if abs(room[cr][cc]-height)>K:  ## 높이 차이 조건
                        continue

                    ## 이 후 탐색할 위치 추가
                    areas.append((cr, cc))

            
    print(NUM)
    


if __name__=='__main__':
    main()