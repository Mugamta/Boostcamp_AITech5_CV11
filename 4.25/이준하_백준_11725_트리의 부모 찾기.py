import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
# 그래프 구성 
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque()
queue.append(1)
parents = [0]*(N+1)

def bfs():
    while queue:
        # queue를 빠져 나오면 현재 노드와 연결된 노드들을 탐색
        parent = queue.popleft()
        for child in graph[parent]:
            # 현재 노드와 연결된 노드들 중에 아직 방문하지 않은 노드들을 queue에 삽입
            if parents[child] == 0:
                parents[child] = parent
                queue.append(child)

bfs()
for i in parents[2:]:
    print(i)