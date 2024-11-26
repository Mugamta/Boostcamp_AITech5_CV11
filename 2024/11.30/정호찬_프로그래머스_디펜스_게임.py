"""
시  간 : 663.67ms
메모리 : 144MB
최대힙을 사용해서 무적권 사용할 수 있고, 힙의 합이 갖고 있는 병사수가 넘어갈때 최댓값을 무적권으로 상쇄하는 방법
만약 무적권을 다썼을때 병사수를 넘어간다면 종료
"""

import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    sum_heap = 0 # 최대힙의 합 연산을 줄이기 위해서
    
    for e in enemy:
        heapq.heappush(heap, (-e, e))
        sum_heap+=e #힙에 값을 넣었다면 sum += value
        
        while (k > 0 and sum_heap > n):
            k-=1
            tmp = heapq.heappop(heap)
            sum_heap-=tmp[1] #제거 되었기 때문에 heap 합에서 빼줌
            
        if (sum_heap > n): #무적권 루프 이후에도 값이 넘어 선다면 종료
            break
        else: # 아니면 라운드 통과
            answer += 1
        
    return answer
