'''
메모리 : 31120KB
시간 : 44ms
'''

def main():
    
    N, S, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cases = set()
    cases.add(S)
    
    ## 각 i번째 볼륨조절 순서에 따라
    for i in range(N):
        
        new_cases = set() # <- deque를 이용하는 경우 메모리 초과, set으로 중복 제거
        
        ## 매 볼륨에 따라 i번째 조절(+,-)이 0~M사이의 볼륨이면 가능한 new_cases로 추가
        for case in cases:
     
            if case+arr[i]<=M:
                new_cases.add(case+arr[i])
            if case-arr[i]>=0:
                new_cases.add(case-arr[i])
        
        ## 현재 갱신된 new_cases를 다음 i+1번째 cases로         
        cases = new_cases
    
    ## 마지막 볼륨 경우의 수들 중 최댓값 출력
    if len(cases):
        print(max(cases))
    else:
        print(-1)
        
    return 0
    
if __name__=='__main__':
    main()
    
    