'''

11:30 시작
그냥 구현 시작

12:20
첫번째 계산은 맞음
두번째 반복부터 오류
-> y dir 설정 오류.. 위쪽이 -, 아래쪽이 +

12:40 완료 

'''

def main():
    
    N, M = map(int, input().split(' '))
    
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split(' '))))
    

    dir = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    dir_corner = [[-1,1],[1,1],[1,-1],[-1,-1]]
    clouds =[[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
    
    ## 구름 이동 반복문
    for _ in range(M):
        num_dir, step = list(map(int, input().split(' ')))
        move_x, move_y = dir[num_dir-1]
        visited = set()
        moved_clouds = []
        
        ## 이전 구름 이동 후, 물의 양 증가(+1)
        for cloud in clouds:
            y, x = cloud
            y = ( y + (move_y*step) )%N
            x = ( x + (move_x*step) )%N
            moved_clouds.append([y,x])      
            visited.add(str(y)+','+str(x))
            mat[y][x] += 1

        ## 구름이 있던 칸의 대각 방향 탐색, 물의 양 update(0~4)
        for cloud in moved_clouds:
            y, x= cloud
            for move_x, move_y in dir_corner:
                check_y = y + move_y
                check_x = x + move_x
                
                ## 물복사 버그는 물이 증가한 칸에 대해서만 시전되므로, 물의 양의 증가가 이후 다른 칸에 시전되는 데에는 영향이 없음
                if check_x>=0 and check_x<N and check_y>=0 and check_y<N and mat[check_y][check_x]:
                    mat[y][x] += 1
        
        ## 바구니 물 2이상인 칸에 대해 구름을 생성, 물의 양 update(-2)
        clouds =[]
        for row in range(N):
            for col in range(N):
                if mat[row][col]>=2 and str(row)+','+str(col) not in visited:
                    mat[row][col] -= 2
                    clouds.append([row,col])

    print(sum([sum([i for i in row]) for row in mat]))
     
main()