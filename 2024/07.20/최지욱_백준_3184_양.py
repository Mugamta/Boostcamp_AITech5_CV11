'''
메모리 : 32864KB
시간 : 112ms
'''

def main():
    
    r, c = map(int, input().split())
    board = [[elem for elem in input()] for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    ## 남은 양과 늑대의 수를 저장
    SHEEP, WOLF = 0, 0
    
    ## 모든 좌표에 대한 탐색
    for row in range(r):
        for col in range(c):
            
            stack = [(row, col)]
            sheep, wolf = 0,0
            
            ## 스택이 비워질때까지(연속된 좌표들을 모두 탐색)
            while stack:
                rr, cc = stack.pop()
                
                if visited[rr][cc]:
                    continue
                
                visited[rr][cc] = True
                
                ## 좌표에서 양, 늑대, 벽을 판단
                if board[rr][cc]=='v':
                    wolf += 1
                elif board[rr][cc]=='o':
                    sheep += 1
                elif board[rr][cc]=='#':
                    continue
                
                ## 탐색 가능한 인접 4방향 좌표들을 스택에 추가 
                for dr, dc in dirs:
                    if 0<=rr+dr<r and 0<=cc+dc<c and not(visited[rr+dr][cc+dc]):
                        stack.append((rr+dr, cc+dc))
            
            ## 한 공간에 양과 늑대의 수에 따라 양과 늑대의 수 업데이트
            if sheep>wolf:
                SHEEP += sheep
            else:
                WOLF += wolf
    
    print(SHEEP, WOLF)
    

if __name__=='__main__':
    main()