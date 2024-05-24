"""
문제 이해 :
    드래곤 커브는 세가지의 속성으로 이루어져 있음
    1. 시작점
    2. 시작 방향
    3. 세대
    
    X축은 → , Y축은 ↓ 
    
    전체 맵의 크기는 100x100
    드래곤 커브가 N개가 있음 
    이때 크기가 1x1인 정사각형의 네 꼭치점이 모두 드래곤커브의 일부인
    정사각형의 개수를 구하는 프로그램을 작성하는 것이 목표이다

구현 방향 :
    1. 드래곤 커브의 정보를 받아서 이를 격자에 그리는것 
    2. 해당 격자에서 정사각형의 갯수를 구하는 것
"""
import sys

def check_value(x, y):
    if (x < 0 or x > 101 or y < 0 or y >= 101):
            return (0)
    else:
        maps[x][y] = 1

def dragon(y, x, d, g):
    check_value(x, y)

    curve = [d]
    for i in range(g):
        for j in range(len(curve) - 1 , -1, -1):
            t_d = (curve[j] + 1) % 4
            curve.append(t_d)
    
    for c in curve:
        x += x_y[c][0]
        y += x_y[c][1]
        check_value(x, y)

def calculate_answer():
    answer = 0
    for i in range(100):
        for j in range(100):
            if (maps[i][j] and maps[i+1][j] and maps[i][j+1] and maps[i+1][j+1]):
                answer+=1
    return (answer)

def solutions():
    n = int(input())
    for _ in range(n):
        y,x,d,g = map(int, input().split())
        dragon(y,x,d,g)
    print(calculate_answer())

if __name__ == '__main__':
    input = sys.stdin.readline
    x_y = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    maps = [[0] * 101 for _ in range(101)]
    solutions()
