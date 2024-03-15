def solution(targets):
    targets = [[e,s] for s,e in targets]
    targets.sort()
    p = -1
    cnt =0 
    
    for e, s in targets:
        if p < s:
            cnt +=1
            p = e-1

    return cnt