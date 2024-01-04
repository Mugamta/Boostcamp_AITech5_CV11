import sys

def rgb() :
    N = int(input())
    arr = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))

    #dp 
    dp = list(list( 0 for _ in range(3)) for _ in range(N) )
    # print("arr", arr)
    # print("dp", dp)
    dp[0] = arr[0] # 맨 처음 집은 자기 자신만 고려 

    for i in range(1, N) : #i 번째 집 : R,G,B 각각을 고려했을 때 가능한 i-1번째의 최소와 더하기
        # i 번째 집의 색을 R,G,B 로 했을때 각각을 구해줘야함. 
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    
    return min(dp[N-1]) # 가장 마지막 집 경우의 수 중 최소를 출력

print(rgb())
