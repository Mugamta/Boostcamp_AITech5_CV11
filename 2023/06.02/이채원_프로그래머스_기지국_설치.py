def solution(n, stations, w):
    answer = 0
    temp = 0
    k = 1 + w*2
    
    for i in stations :
        left = max(1, i-w)
        right = min(n, i+w)
        
        search = left - temp - 1 
        if search :
            answer += search//k
            if search%k != 0 : answer += 1
        
        temp = right
    
    if temp != n :
        search = n-temp
        answer += search//k
        if search%k != 0 : answer += 1
        
        

    return answer