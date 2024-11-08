"""
MST문제 ->Kruskal  알고리즘 문제

문제에서 스패닝 트리는 
n개의 노드로 구성된 그래프가 있다면 해당 그래프는 여러개의 간선으로 구성되어 있을것이다
이중에 최소간선 갯수 (n-1)개로 구성된 그래프 (모든 노드를 연결하면서)를 스패닝 트리라고한다

이때 최소 스패닝 트리는 이러한 가선에 가중치가 있고 해당 가중치의 합이 최소가 되는 
스패닝 트리를 의미하면 MST라고 한다 (스패닝 트리는 여러개가 있을 수 있기 때문에 최소합이 최소 스패닝트리이다)

-> 그래프임에도 트리라고 하는 이유 -> 스패닝 트리는 필연적으로 트리 모양이 되기 때문에

해당 MST를 구하는 알고리즘에는 
Kruskal 과 Prim알고리즘이 있다

Kruskal알고리즘의 경우 Greedy알고리즘으로 우선 가중치를 기준으로 오름차순한 다음
이를 하나씩 추가해 나간다. 이때 추가를 했을때 사이클이 발생하면 이를 제거한다

사이클을 확인하기 위해서는 union-find알고리즘을 이용하면된다

메모리 : 50000 KB
시  간 : 244 MS

"""

import sys

input = sys.stdin.readline

V, E = map(int, input().split())
lines = []
for _ in range(E):
    a, b, weight = map(int, input().split())
    lines.append((a,b,weight))

#weight를 기준으로 오름차순 정렬
lines = sorted(lines, key=lambda x: x[2])

#union-find 알고리즘
parent = [i for i in range(V + 1)]

def get_parent(x):
    if parent[x] == x:
        return (x)
    parent[x] = get_parent(parent[x])
    return (parent[x])

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0

for a, b, w in lines:
    print(parent)
    if not same_parent(a, b):
        union_parent(a, b)
        answer += w
print(answer)
