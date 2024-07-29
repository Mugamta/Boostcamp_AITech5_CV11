from collections import deque, defaultdict, Counter

def solution(topping):
    """
    goal: 롤케이크를 공평하게 자르는 방법의 수 구하기
    note:
        - 롤케이크를 두 조각으로 나누되, 각 조각에 *동일한 가짓수의 토핑이 올라가야 함*
    how:
        - 큐와 사전을 이용한 구현
    """
    n_case = 0
    
    # 효율적인 탐색을 위해 deque, dict 및 count 목적의 변수를 사용
    piece_a, piece_b = deque(), deque(topping)    
    pa_dict, pb_dict = defaultdict(int), dict(Counter(topping))
    n_pa_topping, n_pb_topping = 0, len(pb_dict)
    
    while piece_b:
        t = piece_b.popleft() # 두 번째 조각으로부터 토핑 하나를 꺼내서
        piece_a.append(t) # 첫 번째 조각에 추가함
        
        if not pa_dict[t]: # 기존에 없던, 새로운 종류의 토핑이라면
            n_pa_topping += 1 # 첫 번째 조각의 토핑 종류를 증가
            
        pa_dict[t] += 1 # 첫 번째 조각의 토핑 정보 갱신
        
        pb_dict[t] -= 1 # 두 번째 조각의 토핑 정보 갱신
        
        if not pb_dict[t]: # 더 이상 해당 종류의 토핑이 존재하지 않는다면
            n_pb_topping -= 1 # 두 번째 조각의 토핑 종류를 감소
        
        # 두 조각의 토핑 종류가 같은 경우, count
        if n_pa_topping == n_pb_topping:
            n_case += 1
    
    return n_case