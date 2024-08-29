"""
메모리 : 34148 KB
시  간 : 56 MS
"""

import sys
from collections import deque
input = sys.stdin.readline

# directions -> [0 : 위, 1 : 오,  2 : 아래, 3 : 왼]
def transfer(direction:int, commands:str):
    if commands == 'L':
        direction = (direction - 1) % 4
    elif commands == 'D':
        direction = (direction + 1) % 4
    return direction

def moving(x, y, direction):
    if direction == 0:
        return (x - 1, y)
    elif direction == 1:
        return (x, y + 1)
    elif direction == 2:
        return (x + 1 , y)
    else:
        return (x, y - 1)

N = int(input()) # 맵 크기
K = int(input()) # 사과 갯수

board = list([0] * (N + 1) for _ in range(N + 1))
# 사과 갱신
for _ in range(K):
    i,j = map(int, input().split())
    board[i][j] = 1

transform = deque([])
L = int(input()) # 방향 변환 햇수
for _ in range(L):
    time, t = map(str, input().split())
    transform.append((int(time), t))

# start info setting
result = 0
snakes = deque([(1, 1)])
x,y = 1, 1
board[1][1] = -1
snake_direction = 1
stack = None

while 1:
    if stack is None and transform:
        stack = transform.popleft()
    # trasnfer directions
    if stack is not None and stack[0] == result:
        snake_direction = transfer(snake_direction, stack[1])
        stack = None

    # move snake
    nx, ny = moving(x, y, snake_direction)
    #out of bound
    if (nx <= 0 or nx > N or ny <= 0 or ny > N):
        break
    if (board[nx][ny] == -1):
        break
    
    # update
    if board[nx][ny] == 0:
        tx, ty = snakes.popleft()
        board[tx][ty] = 0
    snakes.append((nx, ny))
    board[nx][ny] = -1
        
    x,y = nx, ny
    result += 1
print(result + 1)
