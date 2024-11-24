"""
최소힙
"""
import heapq

def solution(n, k, enemy):
    answer = 0
    
    pq = []
    for e in enemy:
        # 현재 적보다 남은 병사가 더 많다면
        # 힙에 추가한 뒤, 남은 병사에서 현재 적만큼 차감
        if n >= e:
            heapq.heappush(pq, -e)
            n -= e
            
        # 현재 적보다 남은 병사가 적다면
        else:
            # 무적권이 있는 경우
            if k:
                # IndexError 방지를 위해
                # 일단 현재 적을
                # 힙에 추가한 뒤, 남은 병사에서 현재 적만큼 차감하고
                heapq.heappush(pq, -e)
                n -= e
                
                # 과거의 전투 기록(힙)에서
                # 가장 많은 적과 싸운 기록에 대해
                # 무적권 처리 후, 해당 적의 수만큼 남은 병사를 복원
                n -= heapq.heappop(pq)
                k -= 1
                
            # 무적권이 없으면 종료
            else:
                break
            
        answer += 1
    
    return answer