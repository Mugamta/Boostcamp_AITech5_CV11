"""
메모리 : 31120KB
시간 : 32ms
"""

def main():
    N= int(input())
    M = int(input())
    
    arr =[0]
    for _ in range(M):
        arr.append(int(input()))
    arr.append(N+1)
        
        
    ## 연속된 N개의 좌석으로 앉는 경우의수 dp[N]
    ## 예시 
    ## dp[4] = dp[2] + dp[3]
    ## 4개의 좌석에 앉는 경우의 수 = 3,4번 사람이 자리를 바꾸어 앉는 경우의 수 + 4번 사람이 자리에 그대로 앉는 경우
    dp = [1,1,2]
    for i in range(40):
        dp.append(dp[-1]+dp[-2])
        

    ## 각 연속된 좌석수만큼 경우의 수를 곱함
    result = 1
    for i in range(len(arr)-1):
        L = arr[i+1]-arr[i]
        result *= dp[L-1]
        
    print(result)


if __name__=='__main__':
    main()