import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N,K=map(int,input().split())

tree=[ [] for _ in range(N+1) ]
for i in range(N-1):
    p,c=map(int,input().split())
    tree[p].append(c)
    tree[c].append(p)

apple=list(map(int,input().split()))
visit=[False]*(N+1)

total=0

def DFS(Node,level):
    global total
    visit[Node]=True
    if level<=K and apple[Node]==1:
        total+=1

    for i in tree[Node]:
        if not visit[i]:
            DFS(i,level+1)

DFS(0,0)

print(total)