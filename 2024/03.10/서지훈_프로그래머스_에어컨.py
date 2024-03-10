def solution(temperature, t1, t2, a, b, onboard):
    answer = 10**9
    
    # 승객이 탑승 중인 시간에 쾌적한 실내온도를 유지하기 위한 최소 소비전력
    # 에어컨의 전원이 꺼져있으면 실내온도가 실외온도가 같아지는 방향으로 매분 1도 변화
    # 에어컨의 희망 온도 != 실내온도면 전력 소모 a, 매 분 1도 변화
    # 에어컨의 희망 온도 = 실내온도면 전력 소모 b, 매 분 1도 변화
    
    # onboard의 크기가 1000 -> 2차원 DP?
    
    # DP에는 최소 전력을 저장해야할 것
    # dp[i][j]에서는 onboard의 인덱스가 필요하고, 온도가 필요함...
    # 실내 온도, 희망 온도, 최소 온도, 최대 온도...
    
    # dp[i][j]는 i분일때 온도 j를 만들기 위한 최소 전력?
    
    # 온도의 범위가 -10도가 있으므로, 세 값에 10을 더해주어 음수 인덱스를 해결함
    temperature, t1, t2 = temperature + 10, t1 + 10, t2 + 10
    
    INF = 10**9
    dp = [[INF for _ in range(52)] for _ in range(len(onboard))]
    
    # 0분에 실외온도에 필요한 전력을 0으로 설정
    dp[0][temperature] = 0
    
    for time in range(len(onboard) - 1):
        for degree in range(52):
            # 현재 온도 degree를 만드는 방법...
            # 에어컨 끄기 -> 소모 전력 없음 
            # 에어컨 켜기 (희망온도 일치) -> 전력 소모
            # 에어컨 켜기 (희망온도 불일치)
            
            # 불가능한 온도는 제외
            if dp[time][degree] == INF:
                continue
            
            # 승객이 탑승중인 시간에 t1, t2 사이에 있지 않는 온도는 잘못된 접근이므로 무시함
            if onboard[time] == 1 and not (t1 <= degree <= t2):
                continue
            
            # 온도를 높이는 경우 (50도 이상은 올려도 의미 없음)
            # 1.에어컨으로 조정
            if degree < 50:
                dp[time + 1][degree + 1] = min(dp[time + 1][degree + 1], dp[time][degree] + a)
                # 2. 외부 온도로 조정 (에어컨 끄기)
                if degree < temperature:
                    dp[time + 1][degree + 1] = min(dp[time + 1][degree + 1], dp[time][degree])

            # 온도를 낮추는 경우
            # 1. 에어컨으로 조정
            if degree >= 1:
                dp[time + 1][degree - 1] = min(dp[time + 1][degree - 1], dp[time][degree] + a)
            # 2. 외부 온도로 조정 (에어컨 끄기)
            if degree > temperature:
                dp[time + 1][degree - 1] = min(dp[time + 1][degree - 1], dp[time][degree])

            # 온도를 유지하는 경우
            # 1. 에어컨으로 조정
            dp[time + 1][degree] = min(dp[time + 1][degree], dp[time][degree] + b)
            # 2. 외부 온도로 조정
            if degree == temperature:
                dp[time + 1][degree] = min(dp[time + 1][degree], dp[time][degree])
    
    # 이제 종료 시점 전력을 구하되, 종료 시점에 탑승객이 존재하는 경우 t1 ~ t2를 조사해야 함
    if onboard[-1] == 1:
        print(min(dp[-1][t1:t2 + 1]))
        answer = min(dp[-1][t1:t2 + 1])
    else:  # 아닌 경우는 전체 온도 중 최저 온도 계산
        print(min(dp[-1]))
        answer = min(dp[-1])

    
    return answer