def main():
    
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    
    robots = {}
    dirs = {'E':0,'S':1,'W':2,'N':3}
    step = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}
    
    board = [[False for _ in range(A)] for _ in range(B)]
    
    for num in range(1, N+1):
        x, y, dir = input().split()
        x, y = int(x), int(y)
        robots[num] = [x,y, dirs[dir]] 
        board[y-1][x-1] = num

    for _ in range(M):
        name, order, n = input().split()
        name, n = int(name), int(n)
        x, y, dir  = robots[name]

        if order=='L':
            dir = (dir-n)%4
        elif order=='R':
            dir = (dir+n)%4
        elif order =='F':
            stepx, stepy = step[dir]
            board[y-1][x-1]= False
            
            for _ in range(n):
                x += stepx
                y += stepy
                
                if x<1 or x>A or y<1 or y>B:
                    print(f'Robot {name} crashes into the wall')
                    return 0
                elif board[y-1][x-1]:
                    ex = board[y-1][x-1]
                    print(f'Robot {name} crashes into robot {ex}')
                    return 0
            
            board[y-1][x-1] = name
        
        robots[name]= [x, y, dir]
        
    print('OK')   
    return 0


if __name__ == '__main__':
    main() 