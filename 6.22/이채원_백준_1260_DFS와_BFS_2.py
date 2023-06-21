import sys
from collections import deque

def dfs(V) :     
    print(V, end = ' ')
    visited[V-1] = True
    if len(graph[V-1]) :
        for c in graph[V-1] :
            if visited[c-1] == False :
                dfs(c)
  


def bfs(V) :
    d = deque() 
    d.append(V)
    visited[V-1] = True
    
    while d :
        node = d.popleft()
        print(node, end=' ') 
        
        if len(graph[node-1]):
            for c in graph[node-1] :
                if visited[c-1]==False :
                    d.append(c)
                    visited[c-1]=True
            
    

N, M, V = map(int, sys.stdin.readline().split()) #4 5 1 
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(M)) 
graph = list([] for _ in range(N))

for a,b in arr : #간선 정리
    if b not in graph[a-1] : 
        graph[a-1].append(b)
    if a not in graph[b-1] : 
        graph[b-1].append(a)
for i in range(N) : #간선 정렬
    graph[i].sort()

#visited 배열
visited = list(False for _ in range(N))
dfs(V) 
print()
visited = list(False for _ in range(N))
bfs(V)



