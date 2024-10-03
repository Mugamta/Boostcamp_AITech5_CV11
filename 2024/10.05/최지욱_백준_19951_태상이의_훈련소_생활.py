'''
메모리 : 44180KB
시간 : 172ms (sys.stdin)
'''

import sys

def main():
    
    N, M = map(int, input().split())
    
    ## 흙의 높이 리스트
    arr = list(map(int, input().split()))
    
    ## 칸별 작업의 리스트(덮는 경우 양수, 파내는 경우 음수)
    works = [0 for _ in range(N+1)]
    
    
    ## 조교의 지시 횟수만큼 작업량을 업데이트(누적합 이용 목적)
    '''
    예시 : 
    초기 작업량 누적합  ->  0, 0, 0, 0, 0, 0, 0
    2, 5, 3        ->  0, 2, 0, 0, 0,-2, 0
    시작점을 +k로 종료지점+1 을 -k로 설정
    '''
    for _ in range(M):
        start, end, val = map(int, sys.stdin.readline().split())
        works[start-1] += val
        works[end] -= val
    
    
    '''
    위와 같이 지시사항을 적용한뒤, 누적합으로 연산시
    0, 2, 2, 2, 2, 0, 0
    으로 2~5번째까지의 칸에 작업량 적용결과와 동일
    '''
    prev = 0
    for i in range(len(arr)):
        works[i] = works[i]+prev
        arr[i] += works[i]
        arr[i] = str(arr[i])
        prev = works[i]
            
    print(" ".join(arr))


if __name__=="__main__":
    main()
    