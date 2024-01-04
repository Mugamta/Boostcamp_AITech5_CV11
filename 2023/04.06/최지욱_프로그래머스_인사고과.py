def solution(scores):
    a,b= scores[0]
    prev_b = 0                          ## prev_a = 0
    count = 0
    scores.sort(key = lambda x:(-x[0], x[1]))
    
    for score in scores:
        if score[0]>a and score[1]>b:
            return -1
        elif score[1]>=prev_b:          ## prev_a 비교 필요 X
            prev_b = score[1]           ## prev_a = score[0]
            count += (sum(score)>a+b)
            
    return count+1