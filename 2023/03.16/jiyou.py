def solution(routes):
    answer = 0
    
    routes.sort()
    
    B = -30000
    F = 30000

    for b, f in routes:
        if F < b:
            answer += 1
            
            B = b
            F = f
        else:
            B = max(B, b)
            F = min(F, f)

    return answer + 1