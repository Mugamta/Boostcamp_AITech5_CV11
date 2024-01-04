import sys
from collections import deque


#Tree class 
class Node() :
    def __init__(self) :
        self.child = []  #binary가 아니라 여러개의 child가 있을 수 있어서 리스트로

    def setchild(self, child) : 
        self.child.append(child)

    
        


def apple() :
    #입력
    n, k = map(int, sys.stdin.readline().split())
    arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n-1)) 
    #사과 개수 array
    apple = list(map(int, sys.stdin.readline().split()))
    #Tree의 node 생성
    Tree = list(Node(i) for i in range(n))

    d = deque()
    answer = 0

    for p, c in arr :
        Tree[p].setchild(c)  #해당 index의 node에 set child (self.child 리스트에 append됨.)
    
    d = [[0,0]]  #root 노드 0 

    while d :  #bfs 
        node, distance = d.pop()
        if distance == k : #거리가 k면 굳이 expand 하지 않고 자기자신의 사과만 answer에 더해줌
            answer += apple[node]
        
        elif distance < k : # 거리가 k보다 작으면 사과도 더하고 자식 노드들을 bfs expand
            answer += apple[node]
            for child in Tree[node].child :
                d.append([child, distance + 1])
                
        #거리가 k 이상인 노드는 애초에 deque에 들어오지 않음. 
    return answer 

print(apple())
        


