from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        for _ in range(len(water)):
            x, y = water.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == '.': #맵 안에 있고 빈칸이라면
                    maps[nx][ny] = '*'  # 물로 채우기
                    water.append((nx, ny))  # 다음에 물이 퍼질 위치 추가

        # 고슴도치 이동
        for _ in range(len(q)):
            x, y, time = q.popleft()
            if maps[x][y] == 'D':
                return time  # 도착했을 때 시간 반환
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != '*' and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))

    return "KAKTUS"


r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]

# 초기화
q = deque() #고슴도치
water = deque() #물
visited = [[False] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            q.append((i, j, 0))  # 고슴도치의 위치
            visited[i][j] = True
        elif maps[i][j] == '*':
            water.append((i, j))  # 물의 위치 추가

result = bfs()
print(result)
