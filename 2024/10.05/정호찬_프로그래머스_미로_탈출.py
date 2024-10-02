from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, point, target):
    visted = [[0] * len(maps[0]) for _ in range(len(maps))]
    visted[point[0]][point[1]] = 1
    
    q = deque([(point[0], point[1], 0)])
    while (q):
        x, y, count = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
          
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == target:
                    return (count + 1)

                if not visted[nx][ny] and maps[nx][ny] != 'X':
                    visted[nx][ny] = 1
                    q.append((nx, ny, count + 1)) 
    return (-1)

def solution(maps):
    start, lever, = (), ()
    #좌표구하기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
              
    #출발점에서 L까지 최단거리
    to_lever = bfs(maps, start, 'L')   
    #레버에서 E까지 최단거리
    to_exit = bfs(maps, lever, 'E')
  
    if (to_lever == -1 or to_exit == -1):
        return (-1)
    return (to_lever + to_exit)
