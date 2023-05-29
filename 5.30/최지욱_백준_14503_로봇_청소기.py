def main():
    
    N, M = map(int, input().split(' '))
    r, c, dir = map(int, input().split(' '))
    
    direction = {0:(-1,0),
                 1:(0,1),
                 2:(1,0),
                 3:(0,-1)}
    
    mat =[]
    for _ in range(N):
        row = list(map(int, input().split(' ')))
        mat.append(row)
    
    cleaned = [[0 for _ in range(M)] for _ in range(N)]
    NUM = 1
    
    while True:
        cleaned[r][c]= 1
        
        if 0 not in [cleaned[r-1][c]+mat[r-1][c],
                     cleaned[r+1][c]+mat[r+1][c],
                     cleaned[r][c-1]+mat[r][c-1],
                     cleaned[r][c+1]+mat[r][c+1]]:
            if mat[r-direction[dir][0]][c-direction[dir][1]]==0:
                r -= direction[dir][0]
                c -= direction[dir][1]
                continue
            else:
                break
            
        else:
            dir = (dir-1)%4
            if cleaned[r+direction[dir][0]][c+direction[dir][1]] + mat[r+direction[dir][0]][c+direction[dir][1]] ==0:
                r += direction[dir][0]
                c += direction[dir][1]
                NUM += 1
                
    print(NUM)

main()