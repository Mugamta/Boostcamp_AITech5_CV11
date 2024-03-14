def solution(targets):
    answer = 1
    targets.sort(key = lambda x : [x[0],x[1]] )
    # print(f'targets : {targets}')
    start = targets[0][0]
    end = targets[0][1]
    targets = targets[1:]
    # print(f'new_targets : {targets}')
    
    for s,e in targets :
        if s >= end : #case 1 : 겹치지 않는 경우 
            answer += 1 
            start = s
            end = e
        elif e <= end : #case 2 : 포함되는 경우 
            start = s
            end = e
        else : #case 3 : 겹치는 경우
            start = s    
    return answer