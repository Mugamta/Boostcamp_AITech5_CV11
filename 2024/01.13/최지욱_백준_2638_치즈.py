## 외부를 설정하는 함수
## x,y 좌표를 기준으로 연결된 모든 지점을 'out'으로 설정한 뒤 반환
def get_outside(board, x,y, height, width):
    arr = [(x,y)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while arr:
        x,y = arr.pop()
        if board[y][x]==0:
            board[y][x]='out'
            
            for dy, dx in dirs:
                if (0<=(y+dy)<height) and (0<=(x+dx)<width):
                    if board[y+dy][x+dx]==0:
                        arr.append((x+dx, y+dy))
    return board
        
        
## 전체에서 녹을 대상이 되는 좌표들을 찾아 리스트로 반환하는 함수
def get_melt(board,height, width):
    arr = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    ## 모든 좌표들에 대해
    for y, row in enumerate(board):
        for x, elem in enumerate(row):
            
            ## 좌표가 1이 아닌 경우는 제외
            if board[y][x]!=1:
                continue
            
            ## 좌표가 1인 경우 접한 외부의 수가 2 이상인 경우 리스트에 추가
            cnt =0 
            for dy, dx in dirs:
                if (0<=(y+dy)<height) and (0<=(x+dx)<width):
                    if board[y+dy][x+dx]=='out':
                        cnt+=1
            if cnt>1:
                arr.append((x,y))
    return arr                
        
            


def main():
    
    height, width = map(int, input().split(' '))
    board = [list(map(int, input().split(' '))) for _ in range(height)]
    
    ## 초기 상태에서 외부를 설정
    board = get_outside(board, 0, 0, height, width)
    
    n = 0
    while True:
        n += 1
        
        ## 해당 상태에서 녹을 대상이 되는 위치를 저장한 melt
        melt = get_melt(board, height, width)

        ## 녹지 않은 경우 반복 종료
        if not melt:
            n -= 1
            break
        
        ## 녹은것이 있는 경우 해당 좌표를 0으로 치환하고 
        ## get_outside를 이용하여 그 좌표들로부터 외부로 설정
        for x, y in melt:
            board[y][x] = 0
            board = get_outside(board, x, y, height, width)

    print(n)
    return 0


if __name__ == '__main__':
    main()
