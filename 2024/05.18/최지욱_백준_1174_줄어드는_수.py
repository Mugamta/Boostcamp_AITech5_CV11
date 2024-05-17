'''
메모리 : 31120KB
시간 : 32ms

매번 모든 숫자에 대한 줄어드는 수 판별은 시간적으로 불가능
'''
def main():
    
    N = int(input())
    
    ## 초기 0~9까지의 수
    arr = [str(i) for i in range(0,10)]
    
    ## arr에 숫자를 모두 순회할때까지
    for index, target in enumerate(arr):
        
        ## 원하는 순서의 "줄어드는 수"인 경우 해당 숫자를 출력하고 종료
        if index==N-1:
            print(target)
            return 0
        
        ## 현재 "줄어드는 수"의 뒤에 0~(일의자리수-1) 까지를 덧붙여 arr에 append
        for i in range(0, int(target[-1])):
            arr.append(target+str(i))
    
    ## 해당 순서의 줄어드는 수가 없는 경우 -1 출력        
    print(-1)
    return 0


if __name__ == '__main__':
    main()