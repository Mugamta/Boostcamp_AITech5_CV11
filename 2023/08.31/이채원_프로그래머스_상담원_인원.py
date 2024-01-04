from itertools import combinations_with_replacement

def solution(k, n, reqs):
    answer = []
    
    sd = list(i for i in range(k))
    
    for c in combinations_with_replacement(sd, n-k) :
        ans = 0 
        mt = list(1 for _ in range(k))
        for i in c : 
            mt[i] += 1
        arr = list(list(0 for _ in range(mt[i])) for i in range(k))
        
            
        for start, time, k_ in reqs :   
            
            # print(f"start={start}, time={time}, k={k_}")
            k_ -= 1
            arr[k_].sort()
            # print(f"arr={arr}")
            
            if arr[k_][0] <= start : arr[k_][0]= start + time
            else : 
                ans += (arr[k_][0]-start)
                arr[k_][0] += time
            # print(f"ans={ans}")
        
        answer.append(ans)        
    return min(answer)

