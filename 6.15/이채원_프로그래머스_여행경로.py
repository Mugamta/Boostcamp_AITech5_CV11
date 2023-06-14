def dfs(tickets,used, num, now, array) :
    if num == len(tickets): #모든 Ticket을 다 사용했을 경우
        return array 
    
    #그렇지 않을 경우 
    answer = []
    for i, (a,b) in enumerate(tickets) :
        used_t = used.copy()
        if used_t[i]==False and  now == a : 
            used_t[i] = True

            array_t = array.copy()
            array_t.append(b)
            temp = dfs(tickets, used_t, num+1, b, array_t)
            if len(temp)==len(tickets) + 1 :
                answer.append(temp)
    if len(answer)  :
        answer.sort()
        return(answer[0])
    else : return []
    
            
        
        

def solution(tickets):
    used = list(False for _ in range(len(tickets)))
    answer = dfs(tickets, used, 0, 'ICN', ['ICN'])
    return answer
    
    