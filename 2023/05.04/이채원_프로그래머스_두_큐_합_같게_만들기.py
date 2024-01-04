#프로그래머스 두 큐 합 같게 만들기
from collections import deque
def solution(queue1, queue2):
    answer = 0
    l = len(queue1) * 4
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    if (sum1+sum2) % 2 == 1   : return -1 #전체 합이 홀수면 나눠떨어지지 않음. 
    target =  (sum1+sum2) // 2
    # mx = max(max(q1), max(q2)) #max
    # mn = min(min(q1), min(q2))
    # if mx > target : return -1 #불가능 조건 1
    # if mx != target and mx + mn > target : return -1 #불가능조건2

     
    while True :
        if sum1 == target  : return answer
        elif sum1 > target :
            temp = q1.popleft()    
            q2.append(temp) 
            sum1 -= temp
            sum2 += temp
        else : 
            temp = q2.popleft()
            q1.append(temp)
            sum1 += temp
            sum2 -= temp
        answer += 1
        if answer == l : return -1                                                                                                        
    
    return -1