from collections import deque


def solution(land):
    answer = 0
    
    n = len(land)
    m = len(land[0])
    
    idx = 2  # 몇 번째 구역인지 표기하기 위한 값
    areas = [0, 0]
    
    # BFS를 위한 조건
    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]
    
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1:  # 아직 방문하지 않은 구역이 있다면
                area = 0  # 넓이
                dq = deque()  # BFS를 위한 deque
                
                dq.append((x, y))
                area += 1
                land[y][x] = idx
                
                while dq:
                    X, Y = dq.popleft()
                    
                    for i in range(4):
                        nx, ny = X + plus_x[i], Y + plus_y[i]
                        
                        if 0 <= nx < m and 0 <= ny < n and land[ny][nx] == 1:
                            area += 1
                            land[ny][nx] = idx
                            dq.append((nx, ny))
                
                idx += 1  # 다음 영역으로 변경
                
                areas.append(area)  # 영역별 넓이를 구함
    
    for x in range(m):
        tmps = set()
        for y in range(n):  # 완전탐색으로 각 열마다 어떤 영역이 존재하는지 구함
            tmps.add(land[y][x])
        
        tmp = 0
        for area in tmps:
            tmp += areas[area]  # 구해놓은 영역별 넓이를 더하여 열의 시추량을 구함
        answer = max(answer, tmp)  # 넓이 중 최대 값을 갱신
    
    return answer