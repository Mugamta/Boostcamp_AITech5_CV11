def solution(sticker):
    answer = 0
    
    length = len(sticker)
    
    if length == 1:
        return sticker[0]

    # 길이가 최대 10만 -> 그리디/DP 등 O(NlogN) 이내 해결 가능해야 함
    
    # 뜯어낼 스티커의 개수에 제한이 없음 -> 단, 뜯어낸 스티커의 좌우는 사용 불가
    # 어떤 스티커를 뜯어냈는지에 따라 다음 스티커의 선택이 달라짐 -> DP
    
    # i번째 스티커에서의 최대값은? 
    # 1. i-1번째 스티커를 사용한 경우(i번째 사용 불가)
    # 2. i번째 스티커를 사용한 경우, i-2번째 스티커를 사용 가능
    # 단, 첫 번째 스티커를 떼면 마지막 스티커도 사용 불가
    
    dp1 = [0 for _ in range(length)]
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, length - 1):  # 첫 번째 스티커를 사용하면 마지막 스티커는 사용 불가
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    
    # 첫 번째 스티커를 떼지 않는 경우
    dp2 = [0 for _ in range(length)]
    dp2[0] = 0  # 떼지 않으므로 0이고
    dp2[1] = sticker[1]  # 첫 번째 스티커를 쓰지 않으므로 다음 스티커를 뗌
    for i in range(2, length):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    answer = max(max(dp1), max(dp2))
    return answer