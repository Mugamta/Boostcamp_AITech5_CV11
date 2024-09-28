def solution(n):
    answer = []
    tri = [[0]*i for i in range(1, n+1)]  
    dx, dy = [1, 0, -1], [0, 1, -1] # 아래, 오른쪽, 위
    x, y = 0, 0 # 첫 시작 위치
    num = 1     # 채울 숫자
    d = 0       # 방향 인덱스 (0: 아래, 1: 오른쪽, 2: 위로)
    
    for i in range(1, n*(n+1)//2 + 1):
        tri[x][y] = num
        num += 1
        
        nx, ny = x + dx[d], y + dy[d]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= len(tri[nx]) or tri[nx][ny] != 0:
            d = (d + 1) % 3 
            nx, ny = x + dx[d], y + dy[d]
        
        x, y = nx, ny
    
    for row in tri:
        answer.extend(row)
    
    return answer
