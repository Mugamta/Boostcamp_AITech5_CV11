import copy
import sys
from collections import deque
sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
maps = []
# 0:빈칸 , 1:벽 , 2:바이러스
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    maps.append(list(map(int, input().split())))


def bfs():
    q = deque()
    tmp_maps = copy.deepcopy(maps)

    # 바이러스를 큐에 넣음
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:  # 바이러스인 경우
                q.append((i, j))

    # 바이러스 확산
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 인접한 좌표가 범위 내이고 빈칸이라면 바이러스를 확산시킴
            if 0 <= nx < n and 0 <= ny < m and tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                q.append((nx, ny))

    # 안전 영역 계산
    global ans
    tmp_ans = 0
    for i in range(n):
        tmp_ans += tmp_maps[i].count(0)

    ans = max(ans, tmp_ans)


def makeWall(cnt):
    if cnt == 3:
        bfs()  # 벽이 3개 세워졌을 때 bfs 실행
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:  # 빈칸이라면
                maps[i][j] = 1  # 벽으로 만듦
                makeWall(cnt + 1)  # 다음 벽을 세움
                maps[i][j] = 0  # 복구


makeWall(0)
print(ans)
