def solution(routes):
    camera = -30001
    routes.sort()
    count = 0
    
    for start, finish in routes:
        if start > camera:
            count += 1
            camera = finish
        elif finish < camera:
            camera = finish
            
    return count