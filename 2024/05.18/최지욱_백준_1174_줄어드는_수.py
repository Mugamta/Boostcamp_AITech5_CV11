'''
메모리 : 34000KB
시간 : 64ms

매번 모든 숫자에 대한 줄어드는 수 판별은 시간적으로 불가능
'''
from collections import deque

def main():
    
    N = int(input())
    
    ## 초기 0~9까지의 수
    arr = [str(i) for i in range(0,10)]
    deq = deque(arr)
    num=1
    
    while deq:
        ## queue에서 하나씩 pop
        target = deq.popleft()
        
        ## 원하는 순서의 "줄어드는 수"인 경우 
        if num==N:
            print(target)   ## 현재 순서의 숫자를 출력
            return 0

        ## 현재 순서의 "줄어드는 수"의 뒤에 0~(일의자리수-1) 까지를 덧붙여 deque에 append
        for i in range(0, int(target[-1])):
            deq.append(target+str(i))
        num+=1

    print(-1)
    return 0


if __name__ == '__main__':
    main()