'''
메모리 : 17.9MB
시간 : 56.12ms
'''
def solution(gems):
    length = len(gems)
    types = len(set(gems))  
    nums = dict()
    
    head, tail = 0, 0
    nums[gems[0]] = 1
    shortest = 10000000
    result = [1, len(gems)]
    
    while tail < length:
        if len(nums) == types:
            if tail - head + 1 < shortest:
                shortest = tail - head + 1
                result = [head + 1, tail + 1]
                
            if nums[gems[head]] == 1:
                del nums[gems[head]]
            else:
                nums[gems[head]] -= 1
            head += 1
        else:
            tail += 1
            if tail == length:
                break
            if gems[tail] in nums:
                nums[gems[tail]] += 1
            else:
                nums[gems[tail]] = 1
    
    return result