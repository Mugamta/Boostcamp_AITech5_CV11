def solution(sequence):
    total = 0
    best1 = 0
    best2 = 0
    
    for index, num in enumerate(sequence):
        target = num * (-1)**index
        if target>0:
            total += target 
            best1 = max(best1, total)
        elif total + target < 0:
            total = 0
        else:
            total += target
    
    total =0
    for index, num in enumerate(sequence):
        target = num * (-1)**(index+1)
        if target>0:
            total += target 
            best2 = max(best2, total) 
        elif total + target < 0:
            total = 0
        else:
            total += target
            
    return max(best1, best2)