"""
R x C 의 격자판 

공기 청정기는 1번 열에 설치 -> 크기는 두행을 차지

공기 청정치가 설치 되어 있지 않은 칸에 -> 미세먼지 존재 

미세먼지는 인접한 네방향으로 확산이 된다
인접한 방향에 공기청정기가 있거나 칸이 없으면 그 방향으로 확산이 일어나지 않는다.
확산되는 양은 현재 양 / 5  -> 소수점은 제외
현재 미세먼지가 있는 위치에 남는 미세먼지의 양은 (현재 미세먼지 - (현재 / 5) * 환산되는 방향의 갯수)

"""

import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

input = sys.stdin.readline

# 미세먼지 위치 확인
def check_dust(R, C, maps):
    fine_dust = {}
    for i in range(R):
        for j in range(C):
            if maps[i][j] >= 1:
                fine_dust[(i,j)] = maps[i][j]
    return (fine_dust)

#확산
def diffusions(R, C, fine_dust, maps):
    for key, dust in fine_dust.items():
        x,y = key
        diffus = dust // 5
        # 확산할 위치 체크 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] != -1:
                #확산
                maps[nx][ny] += diffus
                maps[x][y] -= diffus 
    return (maps)

#공기 청정기 작동
def air(R, C, maps, air_xy,  opt='up'):
    if opt == 'up':
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
    else:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
    o_x, o_y = air_xy
    x, y = air_xy
    y += 1
    dir = 0
    before = 0

    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if x == o_x and y == o_y:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue
        maps[x][y], before = before, maps[x][y]
        x = nx
        y = ny
    return (maps)


def run(R, C, T, maps, air_clean):
    for _ in range(T):
        fine_dust = check_dust(R, C, maps)
        maps = diffusions(R, C, fine_dust, maps)
        maps = air(R, C, maps, air_clean[0], "up")
        maps = air(R, C, maps, air_clean[1], "down")

    #calcul
    result = 0
    for i in range(R):
            for j in range(C):
                if maps[i][j] > 0:
                    result += maps[i][j]
    print(result)
            

def main():
    R, C, T = map(int, input().split())
    maps = []
    air_clean = []

    # map parsing
    for i in range(R):
        t_r = list(map(int, input().split()))
        for j in range(C):
            if (t_r[j] == -1):
                air_clean.append((i, j)) # 공기 청정기 위치 저장
        maps.append(t_r)

    run(R, C, T, maps, air_clean)

if __name__ == '__main__':
    main()
