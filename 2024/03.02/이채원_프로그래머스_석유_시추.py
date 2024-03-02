def solution(land):
    answer = 0
    n, m = len(land), len(land[0]) #땅 크기 
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    visited = [list(False for _ in range(m)) for _ in range(n)]

    num = 2 
    size_dict = dict()
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                q = [[i, j]]
                visited[i][j] = True
                size = 0
                
                while q:
                    x, y = q.pop()
                    land[x][y] = num
                    size += 1

                    for a, b in direction: #4방향 탐색
                        dx, dy = x+a, y+b
                        if n > dx >= 0 and m > dy >= 0 and land[dx][dy] == 1 and not visited[dx][dy]:
                            visited[dx][dy] = True
                            q.append((dx, dy))
                            
                size_dict[num] = size
                num += 1

    for i in range(m):
        cand = set()
        
        for j in range(n):
            if land[j][i] != 0:
                cand.add(land[j][i])
        answer = max(answer, sum([size_dict[x] for x in cand]))
    return answer