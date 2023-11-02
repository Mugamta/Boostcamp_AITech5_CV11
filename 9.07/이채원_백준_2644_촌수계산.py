import sys

n = int(input())
A, B = map(int, sys.stdin.readline().split())
m = int(input())
arr = [[] for _ in range(n+1)]
arr_ = []
for _ in range(m) :
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)
visited = list(False for _ in range(n+1))
def dfs(node, d) :
    d += 1
    visited[node] = True

    if node == B :
        arr_.append(d)

    for i in arr[node] :
        if not visited[i] :
            dfs(i, d)

dfs(A, 0)

if len(arr_) == 0 : 
    print(-1)
else :
    print(arr_[0]-1)


