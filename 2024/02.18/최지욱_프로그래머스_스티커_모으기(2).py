def solution(sticker):
    
    if len(sticker)==1:
        return sticker[0]
    elif len(sticker)==2:
        return max(sticker)
    
    dp = [0 for _ in range(len(sticker)-1)]
    dp[0] =sticker[0]
    dp[1] = max(sticker[0],sticker[1])

    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    v1 = dp[-1]
    
    
    dp = [0 for _ in range(len(sticker)-1)]
    dp[0] =sticker[1]
    dp[1] = max(sticker[1],sticker[2])
    
    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i+1])
    v2 = dp[-1]
    return max(v1,v2)