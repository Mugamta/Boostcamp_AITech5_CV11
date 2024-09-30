from collections import deque

def solution(maps):
    # 전처리
    maps = [list(row) for row in maps]
    n, m = len(maps), len(maps[0])
    start, lever, exit = tuple(), tuple(), tuple()
    
    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)
                
    # BFS
    def bfs(r, c, target):
        visited = [[False] * m for _ in range(n)]
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(r, c, 0)])
        visited[r][c] = True
        
        while queue:
            r, c, time2target = queue.popleft()
            
            if (r, c) == target:
                return True, time2target, r, c
            
            for dr, dc in move:
                nr = r + dr
                nc = c + dc
                
                # 보드 벗어남
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                    
                # 방문함
                if visited[nr][nc]:
                    continue
                    
                # 벽
                if maps[nr][nc] == 'X':
                    continue
                    
                queue.append((nr, nc, time2target+1))
                visited[nr][nc] = True
                
        return False, -1, -1, -1
                
    # 시뮬레이션
    can_go2lever, time2lever, lever_r, lever_c = bfs(*start, target=lever)
    if not can_go2lever:
        return -1
    
    can_go2exit, time2exit, _, _ = bfs(lever_r, lever_c, target=exit)
    if not can_go2exit:
        return -1
    
    return time2lever + time2exit


if __name__ == "__main__":
    print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
    print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1
    