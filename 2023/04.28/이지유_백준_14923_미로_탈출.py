from collections import deque

def main():
    # Input.
    N, M = map(int, input().split())

    Hx, Hy = map(int, input().split())
    Ex, Ey = map(int, input().split())

    Hx -= 1
    Hy -= 1
    Ex -= 1
    Ey -= 1

    graph = [input().split(' ') for _ in range(N)]
    
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

    # Compute and Output.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    visited[1][Hx][Hy] = True
    q.append((Hx, Hy, 1, 0))

    while q:
        x, y, is_valid, ts = q.popleft()

        # Check exit condition.
        if Ex == x and Ey == y:
            return ts

        # Move.
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if '0' == graph[nx][ny] and not visited[is_valid][nx][ny]:
                    visited[is_valid][nx][ny] = True;
                    q.append((nx, ny, is_valid, ts + 1))
                elif '1' == graph[nx][ny] and is_valid and not visited[0][nx][ny]:
                    visited[0][nx][ny] = True;
                    q.append((nx, ny, 0, ts + 1))

    return -1

print(main())
