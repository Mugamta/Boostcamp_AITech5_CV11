import sys
from collections import defaultdict

def solution():
    N, M, R = map(int, sys.stdin.readline().split()) #말뚝의 개수 N, 깃대의 개수 M, 현수막 넓이 R
    
    A = list(map(int, sys.stdin.readline().split())) #말뚝의 위치 
    # A.sort()
    B = list(map(int, sys.stdin.readline().split())) #깃대의 길이
    B.sort(reverse = True) #내림차순 정렬
    B = [i/2 for i in B] #삼각형이므로 미리 2로 나눠놓음

    d= defaultdict(int) #밑변 길이 

    for i in range(N-1) :
        for j in range(i+1, N) :
            l = abs(A[j]-A[i]) #밑변 후보
            if l <=R :
                d[l] += 1
    
    answer = -1
    index = 0
    L = list(i for i in d.keys())
    L.sort()

    for l in L : #가장 작은 밑변부터 차례로 
        for h in range(index, M) : #index(가능한 가장 긴 깃대)부터 차례로
            temp = l * B[h] 
            if temp <= R :
                if temp > answer :
                    answer = temp 
                break
            else : index += 1
        if answer == -1 : #가장 작은 밑변을 검사했는데 전부 불가능이면 중단하고 -1 출력
            break
    print(answer)
    
solution()
