import sys
from collections import deque


class UnionFind:
    def __init__(self, n):  # parent의 루트 노드를 자기 자신으로 설정합니다.
        self.parent = [i for i in range(n)]  # 자기 자신을 가르키도록 초기화합니다.

    def find(self, target):  # 루트 노드를 탐색합니다.
        if target == self.parent[target]:  # 부모 노드가 자기 자신, 즉 루트 노드이면 리턴합니다.
            return target
        else:  # 재귀적으로 루트 노드를 탐색합니다.
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a >= b:
            self.parent[a] = b
        else:
            self.parent[b] = a

    def is_union(self, a, b):
        if self.find(a) == self.find(b):
            return True
        return False


p, w = map(int, sys.stdin.readline().split())
c, v = map(int, sys.stdin.readline().split())

uf = UnionFind(p)

dq = deque()

for _ in range(w):
    w_start, w_end, w_width = map(int, sys.stdin.readline().split())
    dq.append((w_start, w_end, w_width))

dq = sorted(dq, key=lambda x: -x[2])
print(dq)

for element in dq:
    uf.union(element[0], element[1])
    print(uf.find(c), uf.find(v), element[2])

    if uf.is_union(c, v):
        print(element[2])
        break
