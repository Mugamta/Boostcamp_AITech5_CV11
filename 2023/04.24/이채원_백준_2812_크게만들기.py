#백준 2812 크게 만들기 

#관찰 1 : 무조건 앞에서부터 한 숫자씩 비교해서 만약 뒤가 더 크면 앞은 삭제하는게 이득
#바꿀만한게 없으면?-> 전체 숫자에 대해서 앞자리가 뒷자리보다 항상 크다는 뜻 -> 그냥 뒤에있는것부터 삭제하면 됨

#deque로 하나씩 옮겨와서 검사

#관찰 2 : 바꿀 기회는 무조건 앞에서 소진하는게 이득이다. 

import sys
from collections import deque


def bignum() :

    N, K = map(int, sys.stdin.readline().split())
    n = input()
    d = deque()
    # n = list(n)

    for i in range(N) : #한글자씩
        # while K>0 :  
        #     if d : 
        #         if d[-1] < n[i] :  
        #             d.pop() #앞 숫자 제거 
        #             K-=1 #기회 소진
        while K>0 and len(d)!=0 and d[-1] < n[i] :
            K-=1
            d.pop()
    
        d.append(n[i])
        
    #다 순회하고 남는 글자는 맨 뒤에서 
    while K>0 : 
        d.pop()
        K-=1
    return ''.join(d)


print(bignum())

