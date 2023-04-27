'''
bfs
2개 2차원 배열
'''
from collections import deque

def main():
    n, m = map(int, input().split())
    o_x, o_y = map(int, input().split())
    d_x, d_y = map(int, input().split())
    board = [input().split(' ') for _ in range(n)]

    ## 2개의 visited 배열 생성(벽을 부순 횟수 0,1)
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    queue = deque([(o_x-1, o_y-1, 0, 0)])       ## x, y, 이동 횟수, 벽을 부순 횟수 
    visited[o_x-1][o_y-1][0] = True             ## 방문 처리
    
    answer =0 
    while queue:
        x, y, count, wall = queue.popleft()

        if (x, y) == (d_x-1, d_y-1):                    ## 목적지 도착시 이동 횟수
            answer = count
            break

        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:      ## 4 방향
            p_x, p_y = x + dx, y + dy

            if not (0 <= p_x < n and 0 <= p_y < m):     ## 범위 이탈 시
                continue

            if (board[p_x][p_y] == '0') and not (visited[p_x][p_y][wall]):      ## 길이고, 방문하지 않은 위치일 때(벽을 부수지 않은 경우, 벽을 부순 뒤)
                visited[p_x][p_y][wall] = True
                queue.append((p_x, p_y, count + 1, wall))   
            elif (board[p_x][p_y] == '1') and (wall == 0) and not (visited[p_x][p_y][1]):       ## 벽이고, 벽을 아직 부수지 않았을 때, 방문하지 않은 위치일 때(벽을 부순 뒤)
                visited[p_x][p_y][1] = True
                queue.append((p_x, p_y, count + 1, 1))

    if answer:
        print(answer)
    else:
        print(-1)

main()
