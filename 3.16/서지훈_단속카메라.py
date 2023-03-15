import copy

def solution(routes):
    routes.sort(key=lambda x : x[1])
    
    answer = 0
    locate = -30001
    
    print(routes)
    
    for route in routes:
        if route[0] <= locate <= route[1]:
            continue
            
        answer += 1
        locate = route[1]
    
    return answer