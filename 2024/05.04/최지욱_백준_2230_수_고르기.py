'''
메모리 : 35364KB
시간 : 124ms
시간 : 4000ms (input())
'''

import sys

def main():
    
    N, M = map(int, input().split())
    arr = []
    
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))
    
    arr.sort()
    
    MIN = 2000000000
    left, right = 0, 1
    
    ## right 지점이 범위를 벗어나기 전까지 반복
    while right<N:
        
        diff = arr[right]-arr[left]
        
        ## 차이가 M 기준과 동일하면 M값 출력 후 조기 종료
        if diff==M:
            print(diff)
            return 0
        ## 차이가 M 보다 크면 최솟값을 갱신하고 left를 증가
        elif diff>M:
            MIN = min(MIN, diff)
            left += 1
        ## 차이가 M 보다 작다면 right를 증가
        elif diff<M:
            right += 1
        
    print(MIN)
    return 0


if __name__ == '__main__':
    main()