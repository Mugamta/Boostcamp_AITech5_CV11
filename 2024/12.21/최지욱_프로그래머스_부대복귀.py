"""
메모리 : 117MB
시간 : 652ms
"""
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    routes ={i+1:[] for i in range(n)}
    shortest =[-1 for _ in range(n+1)]

    for v1, v2 in roads:
        routes[v1].append(v2)
        routes[v2].append(v1)
        
    queue= deque()
    queue.append(destination)
    shortest[destination] = 0
    
    while queue:
        target = queue.popleft()
        for node in routes[target]:
            
            if shortest[node]==-1:
                shortest[node] = shortest[target]+1
                queue.append(node)
            elif shortest[node] <= shortest[target]+1:
                pass
            else:
                shortest[node] = shortest[target]+1
                queue.append(node)
        
    return [shortest[i] for i in sources]