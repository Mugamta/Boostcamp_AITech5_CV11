import sys
from collections import defaultdict

input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())

dic = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)

def search(start, end, visited, answer):
    if start == end:
        return answer
    min_distance = N+1
    visited[start] = True
    for i in dic[start]:
        if not visited[i]:
            result = search(i, end, visited, answer + 1)
            if result != 0:  # 경로를 찾았다면
                min_distance = min(min_distance, result)
    visited[start] = False
    if min_distance != N+1:
        return min_distance
    else:
        return -1  # 경로를 찾지 못했다면 -1 반환

visited = [False] * (N+1)
print(search(a, b, visited, 0))
