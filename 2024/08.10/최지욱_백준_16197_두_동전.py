'''
메모리 : 34280KB
시간 : 60ms

'''

from collections import deque

def main():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    locs = []
    
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'o':
                locs.append((r, c))
                if len(locs) == 2:
                    break
        if len(locs) == 2:
            break

    visited = set()
    queue = deque([(locs[0][0], locs[0][1], locs[1][0], locs[1][1], 0)])
    visited.add((locs[0][0], locs[0][1], locs[1][0], locs[1][1]))

    while queue:
        r1, c1, r2, c2, step = queue.popleft()

        if step >= 10:
            print(-1)
            return

        for dr, dc in dirs:
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc

            out1 = not (0 <= nr1 < N and 0 <= nc1 < M)
            out2 = not (0 <= nr2 < N and 0 <= nc2 < M)

            if out1 and out2:
                continue
            elif out1 or out2:
                print(step + 1)
                return
            else:
                if board[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if board[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2

                if (nr1, nc1, nr2, nc2) not in visited:
                    visited.add((nr1, nc1, nr2, nc2))
                    queue.append((nr1, nc1, nr2, nc2, step + 1))

    print(-1)

if __name__ == '__main__':
    main()