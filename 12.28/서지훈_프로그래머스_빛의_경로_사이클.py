def solution(grid):
    answer = []
    
    # 결국 bfs를 돌아서 이미 방문한 노드라면 필요 없게 됨을 알 수 있음
    # 단, 입출력 예제 1은, 동일 노드에 도착해도 방향에 따라 다른 사이클이 됨
    # 즉 방향이라는 정보가 방문 정보에 필요함
    
    N, M = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(M)] for _ in range(N)]
    
    # 각 위치에서 회전하는 방법...
    # 방향을 0, 1, 2, 3으로 생각할 때, 좌회전은 -1, 우회전은 +1이 되도록 구성하는 것이 편함
    # 따라서 0, 1, 2, 3을 상, 우, 하, 좌로 생각
    
    def rotate(direction, value):
        if value == 'R':  # 우회전하라는 명령을 받은 경우
            direction = (direction + 1) % 4  # 구성한대로 +1을 하되, 값이 4면 3에서 우회전 -> 좌에서 우회전 -> 상
        elif value == 'L':
            direction = (direction - 1) % 4  # 구성한대로 +1을 하되, 값이 -1이면 상에서 좌회전이므로 좌 -> 3 -> % 4
        return direction  # S이면 직진하면 되므로 건드릴 필요 없음
    
    # 상, 우, 하, 좌의 순서대로 좌표 변환
    plus_x = [0, 1, 0, -1]
    plus_y = [-1, 0, 1, 0]
    
    for y in range(N):  
        for x in range(M):  # 모든 노드에 대하여
            for direction in range(4):  # 상하좌우로 움직이는 경우를 조사
                if not visited[y][x][direction]:
                    tmp_x, tmp_y, tmp_direction = x, y, direction
                    length = 0  # 사이클의 길이
                    
                    # 방문하지 않은 지점이라면 사이클을 형성할때까지 이동 반복
                    while not visited[tmp_y][tmp_x][tmp_direction]:
                        visited[tmp_y][tmp_x][tmp_direction] = True  # 방문한 지점 표기
                        length += 1  #  사이클의 길이 증가
                        
                        # tmp_direction에 따라 방향을 움직인 후, 격자의 끝을 넘어가면 반대쪽 끝으로 돌아온다.
                        tmp_x = (tmp_x + plus_x[tmp_direction]) % M
                        tmp_y = (tmp_y + plus_y[tmp_direction]) % N
                        
                        tmp_direction = rotate(tmp_direction, grid[tmp_y][tmp_x])
                        
                    answer.append(length)  # 사이클을 정답에 추가

    answer.sort()  # 오름차순 정렬
    return answer