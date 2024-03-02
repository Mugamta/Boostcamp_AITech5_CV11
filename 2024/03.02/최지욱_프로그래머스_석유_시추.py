def solution(land):
    row = len(land)
    col = len(land[0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    pipes = [[] for _ in range(col)]
    
    for r in range(row):
        for c in range(col):
            if visited[r][c]:
                continue
            if not land[r][c]:
                continue
            
            stack = [[r, c]]
            total = 0
            
            locs = set()
            while stack:
                r, c = stack.pop()
                if land[r][c] and (not visited[r][c]):
                    visited[r][c] = True
                    total += 1
                    locs.add(c)
                else:
                    continue
                
                for dx, dy in dirs:
                    if (0<=r+dy<row) and (0<=c+dx<col):
                        stack.append([r+dy, c+dx])
                            
            for loc in locs:
                pipes[loc].append(total)
                

    return max([sum(pipe) for pipe in pipes])