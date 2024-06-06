import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
heap =[]
for i in range(n):
  t = int(input())
  if t != 0:
    hq.heappush(heap, (abs(t), t))
 
  else:
    if heap:
      tmp = hq.heappop(heap)[1]
      print(tmp)
    else :
      print(0)
    
