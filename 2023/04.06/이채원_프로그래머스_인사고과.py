def solution(scores):    
    answer = 1
    a0,b0 = scores.pop(0) 
    scores.sort(key = lambda x : (-x[0],x[1]))
                
    ta=0
    tb=0
    for i in range(len(scores)) :  
        if ta != scores[i][0] and tb > scores[i][1] :  #둘다 낮으면 인센티브 x
            pass
        else :
            if scores[i][0] > a0 and scores[i][1] > b0 :
                return -1       
            if (scores[i][0]+scores[i][1]) > (a0 + b0) : 
                answer += 1   
            ta = scores[i][0]
            tb = scores[i][1]
    return answer 