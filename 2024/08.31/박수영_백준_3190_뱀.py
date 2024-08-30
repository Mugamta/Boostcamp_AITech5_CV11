import sys
from collections import deque

class Dummy:
    def __init__(self, N, K, board, L, snake_infos):
        self.board_size = N
        self.num_apples = K
        self.board = board

        self.snake_infos = deque(snake_infos)
        self.snake_pos = deque([(0, 0)])

        self.dr = [0, -1, 0, 1]
        self.dc = [1, 0, -1, 0]
        self.direction = 0

        self.time = 0

    def update_direction(self):
        if not self.snake_infos:
            return

        if self.time == self.snake_infos[0][0]:
            _, direction = self.snake_infos.popleft()

            if direction == 'L':
                self.direction = (self.direction + 1) % 4

            elif direction == 'D':
                self.direction = (self.direction + 3) % 4
            
    def move(self, r, c):
        nr = r + self.dr[self.direction]
        nc = c + self.dc[self.direction]

        return nr, nc

    def update_board(self, nr, nc):
        if self.board[nr][nc] == 0:
            tail_r, tail_c = self.snake_pos.popleft()
            self.board[tail_r][tail_c] = 0

        self.board[nr][nc] = 2
        self.snake_pos.append((nr, nc))

    def game_over(self, nr, nc):
        flag = False
        # 보드를 벗어나는 경우
        if nr < 0 or nr >= self.board_size or \
            nc < 0 or nc >= self.board_size:
            flag = True

        # 새 좌표에 뱀이 있는 경우
        elif self.board[nr][nc] == 2:
            flag = True

        return flag

    def game_start(self):
        board[0][0] = 2 # snake

        while True:
            head_pos = self.snake_pos[-1]
            new_pos = self.move(*head_pos)

            self.time += 1
            if self.game_over(*new_pos):
                print(self.time)
                break

            self.update_board(*new_pos)
            self.update_direction()


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input().strip())
    K = int(input().strip())
    
    board = [[0] * N for _ in range(N)]
    for _ in range(K):
        pos_r, pos_c = map(int, input().split())
        board[pos_r - 1][pos_c - 1] = 1

    L = int(input().strip())
    snake_infos = []
    for _ in range(L):
        X, C = input().split()
        snake_infos.append((int(X), C))

    dummy = Dummy(N, K, board, L, snake_infos)
    dummy.game_start()
