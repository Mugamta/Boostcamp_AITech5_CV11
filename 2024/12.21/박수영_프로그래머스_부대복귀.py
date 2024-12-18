"""
그래프
"""
from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    # 그래프 생성
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    # 거리 배열을 -1로 초기화
    dist_list = [-1] * (n+1)
    
    # 목적지를 시작점으로 설정하여 BFS 탐색
    v = [False] * (n+1)
    
    queue = deque([(destination, 0)]) # 현재 위치, 이동한 거리
    v[destination] = True
    dist_list[destination] = 0
    
    while queue:
        region, dist = queue.popleft()
        
        for next_region in graph[region]:
            if v[next_region]:
                continue
                
            queue.append((next_region, dist+1))
            v[next_region] = True
            dist_list[next_region] = dist+1
            
    # BFS 결과 추출 후 반환
    answer = []
    for s in sources:
        answer.append(dist_list[s])
        
    return answer
