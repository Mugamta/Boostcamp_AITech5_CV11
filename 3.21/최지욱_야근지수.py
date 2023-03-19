'''
피로도를 최소화하는 것 -> 작업량의 제곱합을 최소화

제곱합을 최소화하기 위해서는 남은 작업량이 가장 큰 작업부터 줄여야

'''

import heapq

def solution(n, works):
    
    if sum(works) <= n:         ## 작업량 총합이 n시간 이내에 끝마칠 수 있다면
        return 0                ## 남는 피로도는 0
    
    works = [-i for i in works]  
    heapq.heapify(works)            ## max_heap 생성
    
    for i in range(n):
        target = heapq.heappop(works)   ## 가장 높은 값을 가진 작업 pop
        heapq.heappush(works, target+1) ## 가장 높은 값을 가진 작업 수행(-1) 후 push 반복
        
    return sum([i**2 for i in works])   ## 제곱합 return