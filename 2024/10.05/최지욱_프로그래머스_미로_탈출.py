'''
메모리 : 10.4MB
시간 : 10.99ms
'''

from collections import deque

def find(start, end, maps):
    
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    row, col = len(maps), len(maps[0])
    queue = deque([start])
    visited = [[False for _ in range(col)] for _ in range(row)]
    visited[start[0]][start[1]] = 0
    
    while queue:
        r, c = queue.pop()

        for dr, dc in dirs:
            cr, cc = r+dr, c+dc
            
            ## 좌표 범위 조건
            if not (0<=cr<row and 0<=cc<col):
                continue
            
            ## 목표 지점 조건
            if (cr== end[0]) and (cc==end[1]):
                return visited[r][c]+1
            if visited[cr][cc]:
                continue
            if maps[cr][cc]=="X":
                continue
            
            ## cost update
            visited[cr][cc]=visited[r][c]+1
            queue.appendleft([cr,cc])
            
    return -1 
    

def solution(maps):
    
    ## 각 지점(start, end, lever)의 위치 파악
    for index, row in enumerate(maps):
        if "S" in row:
            start = [index, row.index("S")]
        if "E" in row:
            end = [index, row.index("E")]
        if "L" in row:
            lever = [index, row.index("L")]
    
    ## start 지점에서 lever 지점까지
    time1 = find(start, lever, maps)
    ## lever 지점에서 end 지점까지
    time2 = find(lever, end, maps)
    
    ## 둘 중 하나라도 목표 위치로 가지 못하는 경우 -1 return
    if time1==-1 or time2==-1:
        return -1
    
    return time1+time2