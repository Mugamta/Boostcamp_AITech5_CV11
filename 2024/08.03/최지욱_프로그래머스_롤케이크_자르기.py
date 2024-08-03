'''
Worst case
메모리 : 57.2MB
시간 : 551.10ms 
'''

def solution(topping):
    dict = {}
    for num in topping:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    
    n = len(dict)
    
    cnt =0 
    set2 = set()
    for num in topping[::-1]:
        set2.add(num)
        dict[num] -= 1
        if dict[num] ==0:
            n -= 1
        
        if len(set2)==n:

            cnt += 1
        
        if len(set2)>n:
            break
    
    return cnt