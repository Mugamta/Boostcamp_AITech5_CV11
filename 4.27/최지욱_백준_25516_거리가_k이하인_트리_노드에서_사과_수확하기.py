'''
루트에서 depth k이하? bfs
'''
from collections import deque

def main():
    
    n, k = map(int, input().split(' '))
    edge = dict()       ## edge를 담을 dict
    
    
    for _ in range(n-1):        ## edge dict 생성
        
        p1, p2 = map(int, input().split(' '))
        
        if p1 in edge:
            edge[p1].append(p2)            
        else:
            edge[p1] = [p2]
    
    apple = list(map(int, input().split(' ')))
            
    queue = deque([[0,0]])      ## node, depth
    avail = {0}                 ## 수확가능한  node
    
    while queue:
        node, depth = queue.popleft()
        
        if depth>=k:    ## depth가 k이상 깊어지는 경우 break
            break
            
        if node not in edge:    ## node를 부모로 하는 자식이 없을때는 continue
            continue
        
        for child in edge[node]:    ## node를 부모로 하는 자식을 탐색
            queue.append([child, depth+1])  ## 다음 탐색할 queue에 child 정보 append
            avail.add(child)                ## 수확가능한 set에 추가
    
    total =0 
    for i in avail:         ## 수확가능한 set의 apple을 누적
        total += apple[i]

    print(total)
    
main()
