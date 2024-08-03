'''
메모리 : 43848KB
시간 : 100ms
'''

from collections import deque

def main():
    
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()  ## 오름차순 정렬
    
    ## 양방향 출력을 위한 deque
    arr = deque(arr)
    prev = 0
    total = 0
    
    ## (실력이 높은 사람, 실력이 제일 낮은 사람)을 반복하면서
    ## 실력 차이의 합이 최대가 되도록 함
    ## 실력 최상 1위 -> 실력 최하 1위 -> 실력 최상 2위 -> 실력 최하 2위 -> 실력 최상 3위 -> ...
    while arr:
        
        ## (최상의 실력)과 (이전 최하의 실력)차를 누적
        diff = arr.pop()-prev   
        total += diff
        
        ## 이전 최하의 실력 저장
        if arr:
            prev = arr.popleft()
            
    print(total)


if __name__=='__main__':
    main()