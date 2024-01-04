#백준 n11660 구간합구하기5 / 실버1


#13분째 : 아무생각없이 풀고 제출 -> 1% 에서 시간초과 -> 어떻게 해야 연산량을 줄일 수 있을까?
# M 범위가 매우 큼 => 반복되는 연산을 줄여야될듯 -> 동적계획법??
# 53분째 : sum 배열 만들어 식 세워서 풀이 => 성공 !




import sys
from collections import deque
def rangesum() :
    N, M = map(int, sys.stdin.readline().split())
    arrN = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))
    arrM = deque(list(list(map(int,sys.stdin.readline().split())) for _ in range(M)))
    # print("N : ", arrN)
    arrs = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if i==0 and j==0 :
                arrs[j][i] = arrN[0][0]
            elif i == 0 and j != 0 : 
                arrs[j][i] = arrs[j-1][i] + arrN[j][i]
            elif j == 0 and i != 0:  
                arrs[j][i] = arrs[j][i-1] + arrN[j][i]
            else : 
                arrs[j][i] = arrs[j][i-1] + arrs[j-1][i] + arrN[j][i] - arrs[j-1][i-1]
    # print(arrs)
    while arrM :
        x1,y1,x2,y2 = arrM.popleft()
        x1-=1
        x2-=1
        y1-=1
        y2-=1

        if x1 == 0 and y1 == 0 : print(arrs[x2][y2])
        elif x1 == 0 and y1 != 0 : print(arrs[x2][y2] - arrs[x2][y1-1])
        elif x1 != 0 and y1 == 0 : print(arrs[x2][y2] - arrs[x1-1][y2]) 
        else  : print(arrs[x2][y2] - arrs[x1-1][y2] - arrs[x2][y1-1] + arrs[x1-1][y1-1])

rangesum()

