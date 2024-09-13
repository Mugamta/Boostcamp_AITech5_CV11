import sys
from collections import deque
input = sys.stdin.readline

def solution(l, r, c, building):
    """
    goal: 탈출 여부를 구해서 출력
    note:
        - #: 벽, .: 빈칸, S: 시작 지점, E: 출구
        - 각 칸에서 인접한 6개의 칸으로, *1분*의 시간을 들여 이동 가능
    how:
        - BFS
    """
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    move = [(1, 0, 0), (-1, 0, 0), # 층간 이동
            (0, 1, 0), (0, -1, 0), # 행간 이동
            (0, 0, 1), (0, 0, -1)] # 열간 이동
    
    # 시작점, 출구 위치 구하기
    start, end = tuple(), tuple()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    start = (i, j, k)
                    visited[i][j][k] = True # 미리 방문 처리(어차피 큐에 넣을거라)
                
                if building[i][j][k] == 'E':
                    end = (i, j, k)

                if start and end:
                    break

    def bfs():
        queue = deque([(*start, 0)]) # (현재 층, 현재 행, 현재 열, 이동 시간)

        # 탐색
        while queue:
            _l, _r, _c, cnt = queue.popleft()

            # 출구 도착 시 종료
            if (_l, _r, _c) == end:
                return f"Escaped in {cnt} minute(s)."
            
            for dl, dr, dc in move:
                nl = _l + dl
                nr = _r + dr
                nc = _c + dc

                # 범위 벗어나는 경우
                if nl < 0 or nl >= l or \
                    nr < 0 or nr >= r or \
                      nc < 0 or nc >= c:
                    continue

                # 방문한 경우
                if visited[nl][nr][nc]:
                    continue

                # 벽인 경우
                if building[nl][nr][nc] == '#':
                    continue
                
                # 추가 탐색
                queue.append((nl, nr, nc, cnt + 1))
                visited[nl][nr][nc] = True
        
        return "Trapped!"

    return bfs()


if __name__ == "__main__":
    answer = []

    # 입력
    while True:
        L, R, C = map(int, input().split())
        
        # 종료
        if (L, R, C) == (0, 0, 0):
            break

        building = []
        for _ in range(L):
            building.append([list(input().strip()) for _ in range(R)])
            input()

        # 함수 호출
        res = solution(L, R, C, building)

        # 결과 저장
        answer.append(res)

    print(*answer, sep='\n')
    