"""
서로 다른 영역 갯수를 찾으면 되지 않을까

메모리 : 43000 KB
시  간 : 380 MS
"""
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def main():
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = list([0] * M for _  in range(N))
    c = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
               visited = bfs(i, j, N, M, K, visited, board)
               c+=1
    print(c)


def bfs(i, j, N, M, K, visited, board):
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < N and 0<= ny < M and not visited[nx][ny] and abs(board[x][y] - board[nx][ny]) <= K:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return (visited)


if __name__ == '__main__':
    main()