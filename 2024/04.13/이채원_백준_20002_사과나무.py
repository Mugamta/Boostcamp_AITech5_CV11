import sys

N = int(input()) #과수원
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) #총 이익 

dp = list(list(0 for _ in range(N+1)) for _ in range(N+1)) #누적합 배열
for i in range(1,N+1) : #계산상 편의를 위해 1~N+1까지로.
    for j in range(1,N+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1] 

answer = -1001 # -1000 <= 총이익  <= 1000
for i in range(N): #수확하려는 크기 k 
    for row in range(1, N-i+1) :
        for col in range(1, N-i+1) :
            answer = max(answer, dp[row+i][col+i]-dp[row-1][col+i]-dp[row+i][col-1]+dp[row-1][col-1]) #이익이 최대가 되도록

print(answer)
print(dp)
        
