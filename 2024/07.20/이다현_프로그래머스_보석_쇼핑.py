def solution(gems):
    answer = []
    set_gems = set(gems)  # 중복 제거한 보석 종류
    n = len(gems)
    gems_len = len(set_gems)
    dic_gems = {}
    st, end = 0, 0
    min_len = float('inf')

    while end < n:
        if gems[end] not in dic_gems:
            dic_gems[gems[end]] = 1
        else:
            dic_gems[gems[end]] += 1
        
        # 모든 종류의 보석을 포함하게 된 경우
        while len(dic_gems) == gems_len and st <= end:
            if end - st < min_len: #최소 길이라면 업데이트
                min_len = end - st
                answer = [st + 1, end + 1]
            
            dic_gems[gems[st]] -= 1
            if dic_gems[gems[st]] == 0:
                del dic_gems[gems[st]]
            st += 1
        
        end += 1
        
    return answer
