import sys
import heapq

N = int(input())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) #S, T

answer = 1
arr.sort()

heap = []
heapq.heappush(heap,arr[0][::-1])  #first classroom , 끝나는 시간 기준 정렬이 필요하므로 거꾸로 넣어줌


for i in range(1,N) :
    s, t = arr[i]
    if len(heap) : 
        h_t, h_s = heap[0]
        #case 1 : S_i >= heap t : 현재 수업 시작 시간이 heap의 가장 빨리 끝나는 수업보다 뒤일때 -> 강의실 추가배정 필요 없음. 
        if s >= h_t : 
            heapq.heappop(heap)
            heapq.heappush(heap,[t,s])
        #case 2 : S_i < heap t : 가장 빨리 끝나는 수업보다도 먼저 강의실을 써야 함 -> 강의실 추가 배정 필요
        else :
            if len(heap) >= answer :
                answer += 1 #강의실 추가 배정
                heapq.heappush(heap, [t,s])
    # print(f"heap_t={heap[0][0]}, i={i},answer={answer}, s={s}")
            
       
print(answer)

