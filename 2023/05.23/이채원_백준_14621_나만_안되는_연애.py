
import sys


class UnionFind : 
    def __init__(self, N) : 
        self.parent = list(i for i in range(N+1))

    def find(self,x) :
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y) :
        x = self.find(x)
        y = self.find(y)
        if x<y :
            self.parent[y] = x
        else :
            self.parent[x]  = y  
    def is_union(self, x, y) : 
        if self.find(x) == self.find(y) :
            return True
        else :
            return False


def solo():
    edge = [] #edge list 
    for _ in range(M) :
        u, v, d = map(int, sys.stdin.readline().split())    
        if univ[u-1] != univ[v-1] : #W-M이라면 
            edge.append([u,v,d])
    edge.sort(key = lambda x : x[2]) #distance가 짧은 순으로 나열          

    uf = UnionFind(N)        
    Roadnum = 0
    answer = 0
    for u,v,d in edge :
    
        if uf.is_union(u,v) == False : #연결되어있지 않다면 
            uf.union(u,v) #연결
            Roadnum += 1
            answer += d
            
    if Roadnum <N-1 : print(-1)
    else : print(answer)

N, M = map(int, sys.stdin.readline().split())
univ = list(map(str, sys.stdin.readline().split()))

solo()           


