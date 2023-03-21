# 12시 50분 산술기하평균  -> 가장 큰 값부터 줄인다.
# 가장 큰 값 -> 최대 힙 사용 -> 12시 53분 구현
# 12시 57분 1/3 성공
# 12시 58분 answer 초기화 추가 후 성공
# ---------------------------------
# 수학적 증명
# a+b >= 2*sqrt(a*b)
# a**2 + b**2 >= 2*a*b
# (a-b)**2 >= 0 (if a = b : 최소)

from heapq import heappush,heappop,heapify

def solution(n,works):
    # 최대힙 생성
    m_works = list(map(lambda x:-x,works)) 
    heapify(m_works)
    # 남은 시간동안, 가장 큰 일부터 처리
    for _ in range(n):
        a = heappop(m_works)
        # 일 다 끝내면, 야근 없다 ~~
        if a == 0:
            return 0
        heappush(m_works,a+1)
    # 잔업이 있는경우 피로도 도출
    for i in m_works:
        answer += i**2
    return answer

