"""
    메모리 : 34204kb
    시간 : 72ms
"""
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
Gear = [0] + [deque(map(int, input().strip())) for _ in range(T)]
#서로 마주보는 톱니forward일 경우 -> 2번 - 6번, backward일 경우 -> 6번 - 2번

for _ in range(int(input())): #K 번동안 회전
    g_num, direction = map(int, input().split())
    # gear rotation
    b_n, f_n = Gear[g_num][6], Gear[g_num][2]
    o_direction = direction
    Gear[g_num].rotate(direction)

    # 다른 gear rotation
    #backward
    for idx in range(g_num-1, 0, -1):
        if (Gear[idx][2] != b_n):
            b_n = Gear[idx][6]
            Gear[idx].rotate(-(direction))
            direction = -(direction)
        else: #같으면 회전 x 
            break
    #forward
    direction = o_direction #init
    for idx in range(g_num+1, T+1):
        if (Gear[idx][6] != f_n):
            f_n = Gear[idx][2]
            Gear[idx].rotate(-(direction))
            direction = -(direction)
        else: #같으면 회전 x 
            break

#sum
c = sum(Gear[idx][0] for idx in range(1, T+1))
print(c)