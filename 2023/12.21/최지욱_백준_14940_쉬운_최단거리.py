from collections import deque

def main():
    
    n, m = map(int, input().split())
    
    board = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    deq = deque()
    
    for i in range(n):
        board.append(list(map(int, input().split())))
        
        if 2 in board[-1]:  ## 초기 위치(2) 파악
            th = i
            tw = board[-1].index(2)
            
            
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    deq.append([th, tw, 0])
    visited[th][tw]=True
    board[th][tw]=0
    
    while deq:
        h, w, depth = deq.popleft()
        
        ## 4방위 탐색
        for dh, dw in dirs:
            
            ## 탐색 조건 : 지정된 범위 내 / 방문하지 않았을때 / 갈 수 있는 땅일때
            if 0<=h+dh<n and 0<=w+dw<m and not visited[h+dh][w+dw] and board[h+dh][w+dw]:
                board[h+dh][w+dw] = depth+1
                visited[h+dh][w+dw] = True
                deq.append([h+dh, w+dw, depth+1])

    
    ## 고립된 1은 -1(갈수 없는 위치)로 바꾸어주기
    for row in range(n):
        for col in range(m):
            if board[row][col]==1 and not visited[row][col]:
                board[row][col]=-1
    
    ## 출력
    for row in board:
        print(" ".join([str(item) for item in row]))
        
    return 0


if __name__ == '__main__':
    main()