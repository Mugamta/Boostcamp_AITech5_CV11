'''
메모리 : 60400KB
시간 : 348ms
'''

def main():
    r, c = map(int, input().split())
    canvas = [list(map(int, input().split())) for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    NUM = 0
    MAX_AREA = 0
    
    for row in range(r):
        for col in range(c):
            if canvas[row][col] == 0 or visited[row][col]:
                continue
            
            
            stack = [(row, col)]
            area = 0
            
            while stack:
                cr, cc = stack.pop()
                if visited[cr][cc]:
                    continue
                visited[cr][cc] = True
                area += 1
                
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < r and 0 <= nc < c and canvas[nr][nc] and not visited[nr][nc]:
                        stack.append((nr, nc))
            
            NUM += 1
            MAX_AREA = max(MAX_AREA, area)

    print(NUM, MAX_AREA)
    
    
if __name__ == '__main__':
    main()