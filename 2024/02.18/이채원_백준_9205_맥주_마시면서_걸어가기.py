import sys
from collections import deque
t = int(input()) #test 개수 
for _ in range(t) :
    n = int(input()) #맥주를 파는 편의점 개수
    home = list(map(int,sys.stdin.readline().split()))
    store = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    fest = list(map(int, sys.stdin.readline().split()))

    
    d = deque()
    d.append(home)
    done = False
    visited = list(False for _ in range(n))
    while d :
        x, y = d.pop()
        if abs(x -fest[0]) + abs(y - fest[1]) <= 1000 : #종료조건
            done = True
            break
        for s in range(n) :
            if visited[s] == False :
                s_x, s_y = store[s]
                if abs(s_x - x) + abs(s_y - y) <= 1000 :
                    d.append(store[s])
                    visited[s] = True

    if done : print("happy")
    else : print("sad")