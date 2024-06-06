import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    num = int(input())
    if num == 0 : # 작은 값 제거 후 출력
        if not q: #비어있으면
            print(0)
            continue
        abs_num, ori_num = hq.heappop(q)
        print( ori_num)
    else : # 값 넣기
        hq.heappush(q, [abs(num), num])
