import sys
from collections import deque
import math

def solution():
    N = int(input())
    s = list(map(str, sys.stdin.readline().split()))
    s = list([i,1] for i in s)

    A = deque(s)
    B = deque()
    num = 0

    while A : 
        temp = A.popleft()
        if temp[0] == "(" :
            num += 1
            B.append(temp)
            
        elif temp[0] == ")" :
            num -= 1
            if num < 0 or len(B) < 4 :
                return -1

            three = [[0,0],[0,0],[0,0]]
            for i in range(3) :
                three[2-i] = B.pop()
            
            B.pop() # '(' 제거
            B.append(frac(three))

        else : B.append(temp)
    if len(B) >1 : return -1

    return ' '.join(prime(B[0]))

def frac(lst) :
    # a + b / c
    a0 = int(lst[0][0])
    a1 = int(lst[0][1])
    b0 = int(lst[1][0])
    b1 = int(lst[1][1])
    c0 = int(lst[2][0])
    c1 = int(lst[2][1])
    answer = [0,0]
    answer[0] = a0 * b1 * c0 + a1 * b0 * c1
    answer[1] = a1 * b1 * c0
    return answer

def prime(lst): #서로소로 만들기
    x = lst[0]
    y = lst[1]
    if math.gcd(x, y) != 1  : #최대공약수가 1이 아니라면
        x, y = x//math.gcd(x,y) , y//math.gcd(x,y)

    return [str(x), str(y)]
print(solution())