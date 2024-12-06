"""
BFS
"""
from collections import deque

def solution(target_x, target_y, n_pool, pools):
    # 데이터 전처리
    target_x += 500
    target_y += 500

    # 지도 생성
    board = [[0] * 1001 for _ in range(1001)]
    for pool_x, pool_y in pools:
        board[pool_y+500][pool_x+500] = 1 # 웅덩이 기록

    # BFS
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * 1001 for _ in range(1001)]

    queue = deque([(500, 500, 0)]) # 행, 열, 이동 거리
    visited[500][500] = True

    while queue:
        y, x, dist = queue.popleft()

        # 신아의 집에 도착했을 때 종료
        if (y, x) == (target_y, target_x):
            return dist

        # 상/하/좌/우 이동
        for dy, dx in move:
            ny = y + dy
            nx = x + dx

            # 범위 벗어나는지 확인
            if ny < 0 or ny >= 1001 or \
                nx < 0 or nx >= 1001:
                continue

            # 이미 방문한 곳인지 확인
            if visited[ny][nx]:
                continue

            # 웅덩이인지 확인
            if board[ny][nx] == 1:
                continue

            # 추가 탐색
            queue.append((ny, nx, dist+1))
            visited[ny][nx] = True

    return

def main():
    X, Y, N = map(int, input().split())
    pools = [list(map(int, input().split())) for _ in range(N)]

    res = solution(X, Y, N, pools)
    print(res)


if __name__ == "__main__":
    main()
