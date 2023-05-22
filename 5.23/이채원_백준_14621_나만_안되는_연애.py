
import sys
# class Node :
#     def __init__(self, num) :
#         self.num = num 
#         self.parent = num 
#         self.link = []
#         self.road = [None for _ in range(N)]

#     def make_road(self, un, d) :
#         self.link.append(un)
#         self.road.append(d)
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y) :
    x = find(x)
    y = find(y)
    if x<y :
        parent[y] = x
    else :
        parent[x]  = y  


def solo():
    Roads = dict()
    for i in range(M) :
        u, v, d = map(int, sys.stdin.readline().split())    
        if univ[u-1] != univ[v-1] : #W-M이라면 
            if u<v :
                if ((u,v) in Roads and Roads[(u,v)]>d) or (u,v) not in Roads:
                    Roads[(u,v)] = d
            else :
                if ((v,u) in Roads and Roads[(v,u)]>d)  or (v,u) not in Roads:
                   Roads[(v,u)] = d            
            
    Roadnum = 0
    answer = 0
    for u,v in Roads :
        d = Roads[(u,v)]
        if find(u) != find(v) :
            union(u,v)
            Roadnum += 1
            answer += d
    if Roadnum == N-1 : 
        print(answer)
    else : 
        print(-1)

N, M = map(int, sys.stdin.readline().split())
univ = list(map(str, sys.stdin.readline().split()))
parent = list(i for i in range(N+1))
solo()           


