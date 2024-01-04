# [관찰 1] Simulation.

# [관찰 2] 정답의 범위는 [0, 2000]이다.
#          => 처음부터 [0,2000] 범위만 탐색한다.

# [관찰 3] N의 범위는 [1,50]이다.
#          => 필요하다면 충분히 완전탐색할 수 있다.

# [관찰 4] 매일 이루어지는 연산은 2가지이다: 1) 연합 찾기, 2) 연합 내 개별 국가 인구수 갱신하기.
#          => "2) 연합 개 개별 국가 인구수 갱신하기"를 위해서는 [1] 연합 내 개별 국가의 위치, [2] 연합 내 국가의 개수, [3] 연합 내 총 인구수가 필요하다.
#          => "1) 연합 찾기" 시 반드시 A를 완전탐색 해야한다. (완전탐색하는 김에 연합 내 개별 국가의 위치를 담은 리스트와 총 인구수를 구하자.)
#          => "1) 연합 찾기"를 완전탐색 + BFS로 구현한다.          

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# N, L, R, A를 입력받는다.
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 정담 범위를 탐색한다.
for answer in range(2001):
    is_valid = False

    visited = [[False] * N for _ in range(N)]
        
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # BFS를 시행한다.
                q = deque()

                team = [(i, j)]
                total = A[i][j]
                q.append((i, j)) 
                visited[i][j] = True
                    
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx and N > nx and 0 <= ny and N > ny and not visited[nx][ny]:
                            diff = abs(A[x][y] - A[nx][ny])

                            if L <= diff and R >= diff:
                                team.append((nx, ny))
                                total += A[nx][ny]
                                q.append((nx, ny))
                                visited[nx][ny] = True

                # BFS의 시행 결과 연합이 발견되었을 경우, 연합 내 개별 국가의 인구수를 갱신한다.
                if 1 < len(team):
                    is_valid = True

                    avg = total // len(team)
                    for x, y in team:
                        A[x][y] = avg

    # 어떠한 연합도 발견되지 않은 경우, 탐색을 종료한다.
    if not is_valid:
        print(answer)
        break