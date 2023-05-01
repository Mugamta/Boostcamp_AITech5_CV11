import sys
import heapq
input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())


class UnionFind:
    def __init__(self, N):  # parent의 루트 노드를 자기 자신으로 설정합니다.
        self.parent = [i for i in range(N)]  # 자기 자신을 가르키도록 초기화합니다.
        
    def find(self,target):  # 루트 노드를 탐색합니다.
        if target == self.parent[target]:  # 부모 노드가 자기 자신, 즉 루트 노드이면 리턴합니다.
            return target
        else:  # 재귀적으로 루트 노드를 탐색합니다.
            return self.find(self.parent[target])
            
    def union(self,a, b):  # 두 원소를 같은 집합으로 묶습니다.
        self.parent[a] = b  # a의 부모를 b로 설정합니다.
        
    def isUnion(self,a, b):  # 두 원소가 같은 집합에 속하는지 판단합니다.
        if self.find(a) == self.find(b):  
            return True 
        else: 
            return False

graph = UnionFind(p+1)

pq = list()
for _ in range(w):
    n, e, width = map(int, input().split())
    heapq.heappush(pq, (-width, n, e))

while pq:
    cost, start, end = heapq.heappop(pq)
    cost = -cost
    a = graph.find(start)
    b = graph.find(end)
    if a >= b:
        graph.union(a, b)
    else:
        graph.union(b, a)
    
    if graph.isUnion(c, v):
        print(cost)
        break
