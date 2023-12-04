import sys

def solution() :
    N = int(input())
    wine = []
    for _ in range(N) :
        wine.append(int(input()))

    if N <3 : return(sum(wine)) 

    dp = list(0 for _ in range(N))
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max([wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2]])
   
    for i in range(3, N) : 
        temp1 = dp[i-3] + wine[i-1] + wine[i]
        temp2 = dp[i-2] + wine[i]
        temp3 = dp[i-1]
        dp[i] = max([temp1,temp2,temp3])
        
    return dp[N-1]

print(solution())