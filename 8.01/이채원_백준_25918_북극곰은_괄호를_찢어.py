# import sys
from collections import deque

N = int(input()) #문자열 길이
S = list(input()) #문자열

d = deque()
answer = 1

for i in range(N) :
    if len(d)==0: 
        d.append(S[i])
        # answer += 1

    elif d[-1] == S[i] :
        d.append(S[i])
        answer += 1

    else : 
        d.pop()

if d : 
    print(-1)
else :
    print(answer)
