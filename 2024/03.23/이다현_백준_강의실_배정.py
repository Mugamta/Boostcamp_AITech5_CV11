import heapq as hq
import sys
input = sys.stdin.readline
lst = []

n = int(input())
for i in range(n):
  lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:(x[0], x[1]))

heap = [lst[0][1]] #초기값 설정 -> 회의 끝나는 시간

for i in range(1,n):
  #print(lst[i][0], heap)
  if lst[i][0] >= heap[0]: #다음 시작시간이 더 작다면 => 다른 회의실이 필요없을 경우
    hq.heappop(heap)
   
  hq.heappush(heap, lst[i][1])

print(len(heap))
