class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]

    def find(self, target):
        if target == self.parent[target]:
            return target
        else:
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


N, M = map(int, input().split())
MW = [' '] + input().split()
edge_list = []
for _ in range(M):
    edge_list.append(list(map(int, input().split())))

edge_list.sort(key=lambda x: x[2])  # 경로가 짧은 순으로 정렬

uf = UnionFind(N)
result = 0
check = 1

for start, end, length in edge_list:
    # 남초와 여초 대학교를 연결하면서, 이미 연결되어 있지 않은 경우
    if MW[start] != MW[end] and not uf.is_union(start, end):
        uf.union(start, end)
        result += length
        check += 1  # 모든 학교를 연결하는 경로가 있는지 확인

if check < N:
    print(-1)
else:
    print(result)