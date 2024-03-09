def solution(temperature, t1, t2, a, b, onboard):
    #온도 범위가 -10~40이므로, 음수를 고려하지 않기 위해 온도에 10을 더한다. 
    t1 += 10
    t2 += 10
    temperature += 10 
    
    #2차원 DP : row(시간), col(온도)
    dp = [[1e9] * 51 for _ in range(1001)]
    dp[0][temperature] = 0 #시작지점 초기화
    
    for i in range(1, len(onboard)) : 
        #각 시간대에 가능한 시간 범위 지정하기
        start = 0
        end = 0
        
        if onboard[i] == 1 : #승객이 있다면
            start = t1
            end = t2
            
        else : #승객이 없다면
            start = min(t1, temperature)
            end = max(t2, temperature)
        
        for j in range(start, end+1) :
            cost = dp[i][j]
            #dp[i][j]를 만들기 위해 가능한 경우의 수
            
            #case 1 
            #dp[i-1][j-1]로부터 1도 상승해서 dp[i][j]로 오는 경우
            if temperature < j : #실외 온도보다 도달해야 하는 온도가 높다면
                cost = min(cost, dp[i-1][j-1] + a) #에어컨 가동(a 소모)
            else : #실외온도가 더 높다면 에어컨 꺼도 알아서 높아질것 (0 소모)
                cost = min(cost, dp[i-1][j-1])
                
            #case 2 
            #dp[i-1][j]로부터 아무 온도 변화 없이 dp[i][j]로 오는 경우
            if temperature == j : #실외온도와 j가 같다면 에어컨을 꺼도 됨
                cost = min(cost, dp[i-1][j])
            else : #실외온도와 j가 다르다면 b 만큼의 전력이 소모된다. 
                cost = min(cost, dp[i-1][j]+b)
            
            #case 3
            #dp[i-1][j+1]로부터 1도 하강해서 dp[i][j]로 오는 경우
            if temperature > j : #실외 온도가 더 높다면 온도를 1도 내리기 위해 에어컨 가동(a 소모)
                cost = min(cost, dp[i-1][j+1] + a)
            else : #실외 온도가 더 낮다면 에어컨 꺼도 1 낮아질것 (0 소모)
                cost = min(cost, dp[i-1][j+1])
            
            
            dp[i][j] = cost #계산된 최소 cost를 dp에 저장한다. 
            # print(f"dp[{i}][{j}]={cost}")
    
    return min(dp[len(onboard)-1])