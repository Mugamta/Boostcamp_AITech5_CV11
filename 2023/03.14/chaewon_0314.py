#백준 1711 #직각삼각형
import sys
from itertools import combinations

def triangle() :
    N = int(input())
    arr =[]
    for i in range(N) :
        x, y = map(int, sys.stdin.readline().split())
        arr.append([x,y])
    answer = 0
    for (a,b,c) in combinations(arr, 3) :
        length = [(a[0]-b[0])**2 + (a[1]-b[1])**2, (b[0]-c[0])**2 + (b[1]-c[1])**2, (c[0]-a[0])**2 + (c[1]-a[1])**2 ]
        length.sort(reverse = True)
        if length[0] == length[1] + length[2] :
            answer += 1
    return answer 

#입력 받기

print(triangle())

    