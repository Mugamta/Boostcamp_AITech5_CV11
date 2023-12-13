import sys
from collections import deque
import math

def solution():
    N = int(input())
    s = list(map(str, sys.stdin.readline().split()))
    s = list([i,1] for i in s) #맨 처음 정수 입력들은 분모를 1로 가지므로 [분자, 분모(1)] 형태

    A = deque(s)
    B = deque()
    num = 0 #괄호가 몇 개 열린 상태인지 표시하는 변수

    while A : 
        temp = A.popleft()
        if temp[0] == "(" : #case 1
            num += 1 #열린 괄호의 개수 1 증가시킴
            B.append(temp)
            
        elif temp[0] == ")" : #case 2
            num -= 1 #열린 괄호 수 1 감소
            if num < 0 or len(B) < 4 :
                return -1 

            three = [[0,0],[0,0],[0,0]]
            for i in range(3) : #숫자 세 개 (a,b,c) 얻기
                three[2-i] = B.pop()
            
            B.pop() # B 에 들어있는 '(' 제거
            B.append(frac(three)) #a,b,c fraction 연산 완료 후 해당 숫자 다시 넣어놓기

        else : B.append(temp) #case 3 : 숫자는 그대로 넣는다. 

    if len(B) >1 : 
        return -1 #모든 연산 후 숫자 한 개만 남아 있는게 아니라면 오류이므로 -1 출력

    return ' '.join(prime(B[0]))

def frac(lst) : #fraction 연산 a + b / c 
    a0 = int(lst[0][0])
    a1 = int(lst[0][1])
    b0 = int(lst[1][0])
    b1 = int(lst[1][1])
    c0 = int(lst[2][0])
    c1 = int(lst[2][1])

    answer = [0,0] 
    answer[0] = a0 * b1 * c0 + a1 * b0 * c1 #분자
    answer[1] = a1 * b1 * c0 #분모

    return answer

def prime(lst): #서로소로 만들기
    x = lst[0] #분자
    y = lst[1] #분모

    if math.gcd(x, y) != 1  : #최대공약수가 1이 아니라면
        x, y = x//math.gcd(x,y) , y//math.gcd(x,y) 

    return [str(x), str(y)]


print(solution())