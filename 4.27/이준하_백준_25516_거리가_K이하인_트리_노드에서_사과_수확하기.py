import sys
input = sys.stdin.readline

N,K=map(int,input().split())

tree = [ [] for _ in range(N) ]
for _ in range(N-1):
    p,c=map(int,input().split())
    tree[p].append(c)
    tree[c].append(p)

apples = list(map(int,input().split()))

def bfs(graph, start_node):
    distance = 0
    visited = list() 
    queue = list()
    count = 0
    queue.append(start_node) 

    while queue: 
        node = queue.pop(0) 

        if distance > K:
            break

        if node not in visited: 
            visited.append(node)
            queue.extend(graph[node])
            count += apples[node]
        
    # 깊이를 측정하는 방법이 뭘까요!?
        distance += 1

    print("bfs - ", visited)
    return visited
    

bfs(tree, 0)