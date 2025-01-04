'''
메모리 : 121660 KB
시간 : 344 ms
'''
from collections import deque

def main():
    N = int(input())
    '''
    N->1
    dp배열 형태는 [[횟수, 이전값], ...]의 형태로 구성
    '''
    dp = [[0, 0] for _ in range(N+1)]
    dp[N] = [0, 0]
    
    queue = deque([N])
    
    ## N부터 1까지 갈 수 있는 최소 횟수 탐색
    while queue:
        n = queue.popleft()
        if n == 1:
            break
        if n%3 == 0:
            if not dp[n//3][0]:
                dp[n//3] = [dp[n][0]+1, n]
                queue.append(n//3)
        if n%2 == 0:
            if not dp[n//2][0]:
                dp[n//2] = [dp[n][0]+1, n]
                queue.append(n//2)
        if not dp[n-1][0]:
            dp[n-1] = [dp[n][0]+1, n]
            queue.append(n-1)
    
    n = 1  
    result = [1]
    while n != N:
        result.append(dp[n][1])
        n = dp[n][1]
    
    print(dp[1][0])
    print(" ".join(map(str, result[::-1])))

if __name__ == '__main__':
    main()
    