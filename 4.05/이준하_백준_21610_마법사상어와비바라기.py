"""
11:20 풀이 시작
11:27 입출력 받고, 월드, 구름, 방향 8개 설정
11:36 S % N 생각
11:43 2까지 구현
11:46 대각선 구현
11:53 4 구현
00:10 5 구현하면서 3 구현, print 구현
00:12 2번째 부터 move_clouds 생성시 list out of range 에러 발견 및 해결
00:13 테스트 케이스 모두 통과
00:15 정답
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
directions = [(0,0),(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1),(-1, 1),(1, 1),(1, -1)]

for _ in range(M):
    d, s = map(int, input().split())
    move = s % N
    y_move = directions[d][0]*move
    x_move = directions[d][1]*move
    if y_move < 0:
        y_move = N + y_move
    if x_move < 0:
        x_move = N + x_move
    
    move_clouds = []
    for (i,j) in clouds:
        y = i + y_move
        x = j + x_move
        if y >= N:
            y -= N
        if x >= N:
            x -= N
        move_clouds.append((y,x))

    for (i,j) in move_clouds:
        world[i][j] += 1
    for (i,j) in move_clouds:
        for (y,x) in diagonal:
            if 0 <= i+y < N and 0 <= j+x < N and world[i+y][j+x] > 0:
                world[i][j] += 1



    clouds = []
    for i in range(N):
        for j in range(N):
            if world[i][j] >= 2 and (i,j) not in move_clouds:
                world[i][j] -= 2
                clouds.append((i,j))


print(sum(map(sum, world)))

    



