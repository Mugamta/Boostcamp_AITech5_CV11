"""
    메모리 : 39384 KB
    시  간 : 100 MS
"""
from collections import deque
import sys 

input = sys.stdin.readline
target = int(input())
q = deque([[1, 0]]) #화면, 클립보드
vis = [[0] * (target+1) for _ in range(target+1)]

while q:
    window, clip = q.popleft()

    if window == target:
        print(vis[window][clip])
        break

    for i in range(3):
        if i == 0: #1연산
            n_clip, n_window = window, window
        elif i == 1: #2연산
            n_window, n_clip = window + clip, clip
        else: #3연산
            n_window, n_clip = window - 1, clip

        if n_window >= target+1 or n_window < 0 or n_clip >= target+1 or n_clip < 0 or vis[n_window][n_clip]:
            continue 

        vis[n_window][n_clip] = vis[window][clip] + 1
        q.append([n_window, n_clip]) 