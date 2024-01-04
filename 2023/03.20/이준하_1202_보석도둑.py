# 어차피 가방 하나에 보석 하나라고 하면, 가방을 순회하면서, 가방별 보석을 찾으면 된다고 생각.


#12시 20분 시작
#12시 20분 문제 읽기 및 입출력 받기 완료
#12시 38분 작은 가방부터 탐색해야 최적화 가능
#12시 42분 2번째 예제 198 출력 -> 보석을 가방에 담으면 정보에서 제거해야함
#12시 54분 첫 제출 -> 시간초과
#12시 57분 J 정렬 기준 하나로 변경 -> 3% 이후 시간초과
#1시 2분 heapq 사용
#1시 27분 가방에 들어갈 수 있는 모든 보석을 선정하는 경우 최소힙, 들어갈 수 있는 보석 중 가장 비싼 보석을 선정하는 경우 최대힙 사용
#1시 49분 index error
#1시 56분 가방에 들어갈 수 있는 보석이 없는 경우에 대해 예외처리하여 성공



import sys
from heapq import heappop , heappush

N, K = map(int, sys.stdin.readline().split())

J_l = []
B_l = []

for _ in range(N):
    heappush(J_l,list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    B_l.append(int(sys.stdin.readline()))

B_l.sort()

cnt = 0
temp = []
for i in B_l:
    while J_l and i >= J_l[0][0]:
            heappush(temp,-heappop(J_l)[1])
    if temp:
        cnt -= heappop(temp)
    
print(cnt)

    
