#백준 1600 #말이 되고픈 원숭이
from collections import deque
horse = [(-1,-2), (1,-2), (-2,-1), (2,-1), (-2,1), (-1,2), (1,2), (2,1)]
monkey = [(0,-1), (-1,0), (1,0), (0,1)]

#함수
def move(K, W, H, arr ) :  #BFS를 써보자
    q = deque()
    answer =  W + H
    q.append([0,0,0,K]) #(x,y,이동 횟수, 말처럼 이동할 수 있는 횟수)
    while q : # queue에 노드가 없어질떄까지
        x, y, jump, k = q.popleft()
        print("x :", x, " y : ",y, " k : ",k)
        if x == W-1 and y == H-1 : #Target node 인지 확인 
            return jump 
        else : #target이 아니라면 expand해서 모든 자식노드 넣어놓기 
            for i in range(len(monkey)) : #원숭이처럼 이동
                x_n = x + monkey[i][0]
                y_n = y + monkey[i][1]
                if x_n >= 0 and x_n < W and y_n >= 0 and y_n < H and arr[y_n][x_n] == 0 and not (x_n ==0 and y_n ==0) :
                    #갈 수 있다면 노드 추가
                    q.append([x_n, y_n, jump+1 , k])
            if k > 0 : #말처럼 갈 수 있는 횟수가 남아있다면
                for j in range(len(horse)) : #말처럼 이동
                    x_n = x + horse[j][0]
                    y_n = y + horse[j][1]
                    if x_n >= 0 and x_n < W and y_n >= 0 and y_n < H and arr[y_n][x_n] == 0 and not (x_n ==0 and y_n ==0): #갈 수 있다면 노드 추가
                        q.append([x_n, y_n, jump+1 , k-1]) 
    return -1 

#입력받기
print("input :")
K = int(input())
W, H = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(H))
print(move(K, W, H, arr))
