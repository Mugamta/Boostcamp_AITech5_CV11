"""
메모리 : 10.3MB
시간 : 0.09ms
"""
def solution(genres, plays):
    result =[]
    
    dic = dict()
    for i in range(len(plays)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append([plays[i], -i])
        else:
            dic[genres[i]] = [plays[i],[plays[i], -i]]
    arr =[]
    
    for i in dic:
        arr.append((dic[i]))
    arr.sort()
    
    while arr:
        target= arr.pop()[1:]
        target.sort()
        result.append(-target.pop()[1])
        if target:
            result.append(-target.pop()[1])
            
    return result