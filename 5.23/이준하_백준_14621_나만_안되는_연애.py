import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):  # parent의 루트 노드를 자기 자신으로 설정합니다.
        self.parent = [i for i in range(N+1)]  # 자기 자신을 가르키도록 초기화합니다.
        
    def find(self,target):  # 루트 노드를 탐색합니다.
        if target == self.parent[target]:  # 부모 노드가 자기 자신, 즉 루트 노드이면 리턴합니다.
            return target
        else:  # 재귀적으로 루트 노드를 탐색합니다.
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]
            
    def union(self, a, b): # 두 원소를 같은 집합으로 묶습니다.
        a = self.find(a)
        b = self.find(b)
        if a >= b: 
            self.parent[a] = b 
        else:
            self.parent[b] = a
        
    def isUnion(self,a, b):  # 두 원소가 같은 집합에 속하는지 판단합니다.
        if self.find(a) == self.find(b):  
            return True 
        else: 
            return False
        
# 입력 받기
N,M = map(int, input().split())
gender = list(input().split())
road = [list(map(int, input().split()))for _ in range(M)]

# 경로 기준 오름차순 정렬 (최소비용으로 정렬)
road.sort(key = lambda x : x[2])

# 유니온 파인드
school = UnionFind(N)
answer = 0

# 최소 비용의 두 원소를 연결했을 때 사이클이 아니라면 연결
for u, v, d in road:
    if not school.isUnion(u, v):
        #남자학교 여자학교인경우
        if gender[u-1] != gender[v-1]:
            school.union(u, v)
            answer += d
# 연결되지 않은 노드가 있는 경우 -1 출력
for i in range(1, N+1):
    if school.find(i) != school.find(1):
        answer = -1
        break
# 모든 원소가 연결되면 종료합니다.
print(answer)
