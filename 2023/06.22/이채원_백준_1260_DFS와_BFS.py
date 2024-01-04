import sys
from collections import deque
def dfs(V) :     
    print(V, end = ' ')
    visited[V-1] = True
    if len(graph[V-1]) :
        for c in graph[V-1] :
            if visited[c-1] == False :
                dfs(c)


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


#DFS
visited = list(False for _ in range(N))
# d = deque()
# d.append(V)
# answer = []

# while d :
#     temp = deque()
#     node = d.popleft()
#     visited[node-1] = True
#     answer.append(str(node))
#     if len(answer) == N :
#         print(' '.join(answer))
#         break
#     if len(graph[node-1])== 0 :
#         continue
#     else : 
#         for c in graph[node-1] :
#             if visited[c-1]==False :
#                 temp.append(c)
                

#     while temp : 
#         d.appendleft(temp.pop())  
    

dfs(V)
print()


visited = list(False for _ in range(N))
d = deque()
d.append(V)
answer = []

while d : #BFS
    node = d.popleft()
    visited[V-1] = True
    answer.append(str(node))
    if len(graph[node-1])==0 :  #더이상 갈 수 있는 노드가 없을 때
        continue
    else : #갈 수 있는 노드가 있을 때
        for c in graph[node-1] :
            if visited[c-1] == False : 
                d.append(c)
                visited[c-1] = True
print(' '.join(answer))
    
        