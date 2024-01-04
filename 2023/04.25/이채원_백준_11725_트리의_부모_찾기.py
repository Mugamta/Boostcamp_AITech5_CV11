import sys

#tree 구현
class Node :
    def __init__(self, parent = None) :
        self.parent = parent


def find() :
    N = int(input())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
    # print(arr)
   
    nodes = [None for _ in range(N)]
    nodes[0] = Node("root")
    
    
    for A, B in arr :
        if nodes[A-1]!= None and nodes[B-1] != None : continue
        elif nodes[B-1] == None : #A는 생성, B는 생성 전
            nodes[B-1] = Node(parent = A)
        else : #A 생성 전
            if nodes[B-1] != None :
                nodes[A-1] = Node(parent = B)

    for j in range(1, N) :
        print(nodes[j].parent)



find()