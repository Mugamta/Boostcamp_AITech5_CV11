from collections import deque

def main():
    start, end = map(int, input().split())
    
    if start == end:                    ## 시작, 종료가 같은 지점인 경우
        print(0)                        ## depth 0 출력
        return

    N, M = map(int, input().split())

    graph = {i: set() for i in range(1, N+1)}  # 인접 정점을 집합으로 변경

    ## 그래프 생성
    for _ in range(M):
        char1, char2 = map(int, input().split())
        graph[char1].add(char2)  
        graph[char2].add(char1)  
    #################
    
    visited = set()     ## 방문 처리 용
    depth = 0
    queue = deque([start])

    while queue:
        level_size = len(queue)
        for _ in range(level_size):     ## 동일 깊이(level)에서 갈 수 있는 노드 순회
            head = queue.popleft()      ## 시작 노드
            if head == end:             ## 도착 지점 찾은 경우  
                print(depth)            ## depth를 출력
                return 0
            visited.add(head)           ## 방문처리           
            
            for i in graph[head]:       ## 갈 수 있는 경로를 탐색
                if i not in visited:    ## 방문하지 않은 경우
                    queue.append(i)     ## queue에 추가하고
                    visited.add(i)      ## 방문 처리
        depth += 1

    print(-1)       ## 도달할 수 없는 경우

main()