from collections import defaultdict

def solution(gems):
    """
    goal: 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾기
    note:
        - 구간 >> 연속되어야 함
        - 짧은 구간이 여러 개인 경우, 시작 진열대 번호가 가장 작은 구간을 반환
    how:
        - 투 포인터 + dictionary 활용
    """
    # 모든 보석을 하나 이상 포함하는 구간들을 저장
    candidates = []
    
    # 모든 보석을 하나 이상 포함하는 구간 찾기
    n_jewels = len(set(gems)) # 전체 보석 종류의 수
    cnt = 0 # 카트에 담아둔 보석 종류의 수
    
    cart = defaultdict(int) # 담은 보석을 기록할 dict
    start, end = 0, 0 # 투 포인터
    
    # 범위 내에서 탐색을 진행
    while start <= end and end < len(gems):
        if cnt == n_jewels: # 카트에 담아둔 보석 종류의 수와 전체 보석 종류의 수가 같다면
            candidates.append([start+1, end]) # 구간을 추가함
            
            # 가장 짧은 구간을 찾기 위해서, 앞쪽 보석을 뺌
            cart[gems[start]] -= 1
            if not cart[gems[start]]: # 그로 인해 해당 종류의 보석이 더 이상 없다면
                cnt -= 1 # 카트에 담아둔 보석 종류의 수를 감소
                
            start += 1 # 앞쪽 포인터를 증가
            
        else: # # 카트에 담아둔 보석 종류의 수와 전체 보석 종류의 수가 다르다면
            if not cart[gems[end]]: # 새로운 보석인 경우
                cnt += 1 # 카트에 담아둔 보석 종류의 수를 증가
                
            cart[gems[end]] += 1 # 카트에 보석을 추가하고
            end += 1 # 뒤쪽 포인터를 증가
    
    # 탐색 범위로 인한 예외를 처리하기 위해, while 문을 이용하여 최종 탐색
    while cnt == n_jewels:
        candidates.append([start+1, end])
            
        cart[gems[start]] -= 1
        if not cart[gems[start]]:
            cnt -= 1

        start += 1
    
    # (구간의 길이, 시작 진열대 번호) 순서대로 정렬
    candidates.sort(key=lambda x: (abs(x[1] - x[0]), x[0]))
    
    return candidates[0]


# print(solution(list("A B B B C D D D D D D D B C A".split())))