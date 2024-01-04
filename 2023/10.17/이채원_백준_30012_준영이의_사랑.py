import sys
from collections import deque

N= int(input())
P = list(map(int, sys.stdin.readline().split())) #N개 진주알의 가치

P.sort(reverse = True)
# print(f"P:{P}")

ans = deque()
temp = False 

#목걸이 배열하기
ans.append(P[0]) 
for i in range(1,N) :
    if temp :
        ans.append(P[i])
        temp = False

    else :
        ans.appendleft(P[i])
        temp = True

#목걸이 가치 계산하기
answer = 0
ans_ = []
ans_.append(str(ans[0]))
for i in range(1,N) :
    answer += ans[i-1] * ans[i]
    ans_.append(str(ans[i]))
answer += ans[-1] * ans[0]

print(answer) 
print(' '.join(ans_)) 






