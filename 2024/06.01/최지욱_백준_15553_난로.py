'''
메모리 : 35364KB
시간 : 100ms
'''

import sys

def main():
    
    N, K = map(int, input().split())
    
    ## 첫 값을 이전 값으로 먼저 초기화
    prev = int(input())
    arr = []
    
    ## 이후 입력들에 대해서 전 시간과의 차이(diff)를 리스트에 추가
    for _ in range(N-1):
        num = int(sys.stdin.readline())
        diff = num - prev
        
        ## diff-1로 추가
        arr.append(diff-1)
        prev = num
    
    ## 시간차이를 내림차순으로 정렬(뒷 쪽값이 제일 작도록)
    arr.sort(reverse=True)
    
    ## 성냥이 N개 있다고 가정하고, 각각 1의 시간 만큼 켜져있다고 있다고 가정한 뒤,
    ## 부족한 성냥의 개수(N-K)만큼, 각 시간 차이를 이어주도록 함
    ## 작은 차이부터 순서대로 뽑아가면서 이어주어야 하는 횟수(N-K)만큼 더해줌
    for _ in range(N-K):
        N += arr.pop()
    
    ''' 예시
    N=3, K=2
    [1, 3, 6] 에서 각 시각에 1시간 불을 켰다고 가정하고(N시간), 줄여야하는 성냥 개수(N-K=1) 만큼
    작은 차이(3-1-1=1)만큼을 N에 더해줌
    
    '''
    print(N)


if __name__ == '__main__':
    main()