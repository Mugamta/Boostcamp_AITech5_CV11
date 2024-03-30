from itertools import product
from copy import deepcopy
import sys

dx = [0, 0, 0, 1, -1]
dy = [0 ,1, -1, 0, 0]

def rotate(x, y, arr, r_n, n):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            arr[ny][nx] = (arr[ny][nx] + r_n) % 4 

def solution(clockHands):
    answer = sys.maxsize
    n = len(clockHands)
    
    for p_c in product(range(4), repeat=n):
        tmp = 0
        board = deepcopy(clockHands)
        
        #첫번째 행 돌리기
        for idx in range(n):
            if not p_c[idx]:
                continue
            tmp += p_c[idx]
            rotate(idx, 0, board, p_c[idx], n)
        
        #순서대로 위행의 결과를 중심으로 조작
        for y in range(1, n):
            for x in range(n):
                #0 -> 0, 1->3, 2->2, 3-> 1
                r_n = (4 - board[y-1][x]) % 4
                if not r_n:
                    continue
                tmp += r_n
                rotate(x, y, board, r_n, n)

        # 마지막 행에 0이 있는지
        if any(board[-1]):
            continue
        # 없다면 갱신
        answer = min(tmp, answer)
            
    return answer

"""
1) 4번 이상 회전 하는 것은 사실 무회전임
2) 같은 행에 있다면 누르는 순서는 결과에 영향을 주지않음
3) n-1 행은 n 행에 종속적이다 (1행은 2행에, 2행은 3행에)
4) 따라서 첫행의 방향이 어떤지에 따라서 아래의 행이 결정된다
5) 마지막 행의 결과는 결국 첫행이 어떻게 구성되느냐임
6) 따라서 첫행의 경우의 수를 완전탐색하고 2행씩 내려가면서 조작해보면된다.
"""