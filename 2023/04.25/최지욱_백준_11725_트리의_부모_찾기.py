'''
11:10
11:55
'''
from collections import deque

def main():
     
    n = int(input())
    edge = dict()       ## edge를 담을 dict
    
    for _ in range(n-1):        ## edge dict 생성
        
        p1, p2 = map(int, input().split(' '))
        
        if p1 in edge:
            edge[p1].append(p2)            
        else:
            edge[p1] = [p2]
                
        if p2 in edge:
            edge[p2].append(p1)            
        else:
            edge[p2] = [p1]
            
            
    parent = dict()     ## parent 정보를 담을 dict {child:parent}
    queue = deque([1])  ## root부터 시작할 queue
    
    
    while queue:
        node = queue.popleft()      ## 탐색할 node(parent)  
        
        for child in edge[node]:    ## node와 연결된 child를 탐색
            if child not in parent: ## child가 parent를 아직 못 찾은 경우
                parent[child]= node ## child의 parent값을 저장
                queue.append(child) ## child를 다음 탐색할 queue에 append
        
    for i in sorted(parent)[1:]:    ## 2의 parent부터 출력
        print(parent[i])
        
main()