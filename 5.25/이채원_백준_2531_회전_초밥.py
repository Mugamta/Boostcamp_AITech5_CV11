#1am start
#1:30 첫 제출 -> 시간 초과
#1:37 arr를 rotate하고 temp를 매번 새로 지정하던 방식을 수정 -> 틀림
#1:45 k를 고정하고 풀고 있던 실수 발견


import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(N))

d = deque(arr) #초밥 벨트 deque로 
answer = 0
temp = deque(arr[:k])

for i in range(N) :

    if c not in temp : #쿠폰번호 포함되어있지 않으면
        num = len(set(temp)) + 1
    else : 
        num = len(set(temp))
    if answer < num : 
        answer = num    
    if answer ==  k + 1 : break


    # d.rotate(-1)

    d.append(temp.popleft())
    temp.append(d[k+i])
    
print(answer)

