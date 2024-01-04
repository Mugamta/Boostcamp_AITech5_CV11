import sys
from collections import deque

N = int(input())
a = input()
arr_ = list(a)

arr = deque()
for i in range(N) : 
    if arr_[i]=='#' :
        arr.append(i+1)

answer = 0
print(arr)

while arr :
    answer += 1
    temp = arr.popleft()
    d = deque()

    for i in range(len(arr)) :
        k = arr.popleft()
        if k%temp != 0 :
            d.append(k)

    arr.extend(d)

print(answer)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              