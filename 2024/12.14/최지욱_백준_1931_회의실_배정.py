"""
메모리 : 46628KB
시간 : 228ms
"""
import sys

def main():

    N = int(input())
    arr = []
    
    for _ in range(N):
        start, end = map(int,sys.stdin.readline().split())
        arr.append([start, end])
    
    ## 스케줄을 시작시간, 종료시간 오름차순으로 정렬
    arr.sort()
    
    N =0 
    tail = 0
    
    for start, end in arr:
        ## 해당 회의시작 시각이 최종 종료시각보다 뒤인 경우
        ## 회의 수를 1 증가하고, 해당 회의 종료시간으로 최종 종료시각을 업데이트
        if start>=tail:
            N+=1
            tail = end
        else:
            ## 해당 회의종료 시각이 최종 종료시각보다 먼저 끝나는 경우
            ## 이전 회의의 최종 종료시각을 해당 회의 종료시각으로 교체
            if tail>end:
                tail=end
                
    print(N)    
    return 0
    
if __name__ == '__main__':
    main()
