import sys
from collections import deque

def solution():
    T = int(input()) #Test 개수 T
    test_ = list(list(list(map(str, sys.stdin.readline().split())) for _ in range(3)) for _ in range(T))
    #Head 를 1로, Tail을 0으로 변환
    for i in range(T) :
        for j in range(3) :
            for k in range(3) :
                if test_[i][j][k] == 'H' : test_[i][j][k] = '1'
                elif test_[i][j][k] == 'T' : test_[i][j][k] = '0'
    #test 차원 축소 (3->2)
    test = []
    for i in range(T) :
        temp = []
        for j in range(3) :
            temp += test_[i][j]
        test.append(temp)
    # print(test)

    for i in range(T) : 
        root = test[i] 

        d = deque()
        visited = list(False for _ in range(512)) # "000000000"~"111111111"까지 총 2^9가지 경우의 수
        visited[int(''.join(root),2)] = True #root node visit 처리
        d.append([root, 0]) #root node 넣고 BFS 시작하기

        done = False #solution 찾을 수 있는지 여부를 나타내기 위한 변수
        #BFS
        while d : 
            node, num = d.popleft()
            
            if node == ["0","0","0","0","0","0","0","0","0"] or node == ["1","1","1","1","1","1","1","1","1"] : #조건 만족한다면, 그게 곧 가장 빠른 길이므로 BFS 중단
                done = True
                break
           
            for j in range(8) :  #조건 만족하지 않는다면 extend : 8가지 FLIP 시도
                new_node = flip(node, j) 
                if visited[int(''.join(new_node),2)] == False : 
                    visited[int(''.join(new_node),2)] = True
                    d.append([new_node, num+1])
            
        if done == True : 
            print(num)
        else : 
            print(-1)        

flip_case = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #뒤집는 경우의 수(각 행, 열 또는 대각선), 9개의 coin 중 뒤집을 index 3개를 나타냄.

def flip(node, i) : #동전 뒤집기
    temp = node.copy() #node 손상되지 않도록 copy 사용!

    for j in range(3) : #flip case i에 따라 뒤집을 동전의 index 3개 뒤집기

        if node[flip_case[i][j]] == '1' : 
            temp[flip_case[i][j]] = '0'

        elif node[flip_case[i][j]] == "0" :
            temp[flip_case[i][j]] = "1"

    return temp 

solution()