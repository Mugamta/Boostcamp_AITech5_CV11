# 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 한칸 뒤에서 1번 반복 혹은 중지
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 90도 회전, 한칸 전진, 1번 반복

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
r, c, d = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
move = [(-1,0),(0,1),(1,0),(0,-1)]

while True:
    visited[r][c]= 1
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 한칸 뒤에서 1번 반 복 혹은 중지
    if 0 not in [visited[r-1][c]+world[r-1][c],
                    visited[r+1][c]+world[r+1][c],
                    visited[r][c-1]+world[r][c-1],
                    visited[r][c+1]+world[r][c+1]]:
        if world[r-move[d][0]][c-move[d][1]]==0:
            r -= move[d][0]
            c -= move[d][1]
            continue
        else:
            break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 90도 회전, 한칸 전진, 1번 반복
    else:
        
        if d == 0:
            d = 3
        else:
            d -= 1
        
        if visited[r+move[d][0]][c+move[d][1]] + world[r+move[d][0]][c+move[d][1]] ==0:
            r += move[d][0]
            c += move[d][1]
            
print(sum([sum(row) for row in visited]))

