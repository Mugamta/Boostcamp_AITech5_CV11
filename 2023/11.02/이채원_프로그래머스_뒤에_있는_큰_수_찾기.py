from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    d = deque()
    
    for i in range(len(numbers)) :
        num = numbers[i]        
        while d :
            if numbers[d[-1]] < num :
                answer[d.pop()] = num 
            else :
                break
        d.append(i)
        
    return answer