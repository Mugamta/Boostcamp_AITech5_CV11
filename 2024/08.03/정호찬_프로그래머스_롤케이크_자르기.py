"""
  메모리: 56.9MB
  시  간: 587.25ms
"""
from collections import deque,  Counter

def solution(topping):
    c = 0
    
    b = deque(topping)
    s_a, s_b = set(), dict(Counter(topping))
    while (b):
        t = b.popleft()
        s_a.add(t)
        
        if (s_b[t] > 1):
            s_b[t] -= 1
        else:
            del s_b[t]
        
        if (len(s_a) == len(s_b)):
            c+=1
        
    return (c)
    
