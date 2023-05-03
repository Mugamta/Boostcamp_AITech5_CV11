'''
시간 초과
'''

from collections import deque

def solution(queue1, queue2):
    
    total = sum(queue1) + sum(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if total%2==1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count =0 
    
    history = set()
    
    while sum(queue1) != total//2:
        if tuple(queue1) in history:
            return -1
        
        history.add(tuple(queue1))
        count += 1
        
        if sum(queue1) > total//2:
            queue2.append(queue1.popleft())
        else:
            queue1.append(queue2.popleft())
        
    return count