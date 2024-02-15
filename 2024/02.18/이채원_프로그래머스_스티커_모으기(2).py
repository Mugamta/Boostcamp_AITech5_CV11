def solution(sticker):
    # answer = 0
    N = len(sticker)
    
    if N==1:
        return sticker[0]
    if N ==2 :
        return max(sticker[0], sticker[1])
    #case 1 : 맨 뒤 원소가 없다고 생각하기
    dp1 = list(0 for _ in range(N-1))
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, N-1) :
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])   
    
    #case 2 : 맨 앞 원소가 없다고 생각하기
    dp2 = list(0 for _ in range(N))
    dp2[1] = sticker[1]
    dp2[2] = sticker[2]
    for i in range(3, N) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    return max(dp1[-1], dp2[-1])