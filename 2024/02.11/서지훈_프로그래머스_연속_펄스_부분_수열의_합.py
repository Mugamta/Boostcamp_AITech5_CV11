def solution(sequence):
    answer = 0
    
    # 길이가 50만 -> 그리디, DP, 자료구조 등 O(NlogN)
    
    # 연속 펄스 부분 수열의 합 중 가장 큰 것 -> DP (모든 펄스 부분 수열 중 가장 큰 것)
    
    # "연속"된 부분 수열 -> 반드시 1, -1의 형태로 구성됨...
    # 즉, 원본 배열 * (1, -1, 1, -1)...의 형태로 구성되거나, (-1, 1...)의 형태로 구성
    # [2, -3, 6, -1, 3, 1, 2, -4]
    # [-2, 3, 6, 1, -3, 1, -2, 4]
    
    # 이 중 최대가 되는 구간의 합을 찾기
    # -> dp[i] = dp[i - 1] + arr[i]로 더해나가면, dp[i-1]이 음수가 될 수 있음 (ex) -2로 시작하는 경우)
    # 따라서 이전 값이 음수이면 arr[i]를 선택하여 이전 값을 버림
    # 또한 구간의 합이 중간에서 등장할 수 있으므로, answer을 중간에서 갱신하거나 dp를 돌린 후 마지막에 찾아야 함
    
    length = len(sequence)
    dp1 = [sequence[i] * (-1) ** (i % 2) for i in range(length)]
    dp2 = [sequence[i] * (-1) ** (i % 2 + 1) for i in range(length)]
    
    for i in range(1, length):
        # dp에 바로 덮어씌우면 추가 메모리 필요 없음, 리스트 초기화 시간 필요 없음
        dp1[i] = max(dp1[i - 1] + dp1[i], dp1[i])
        dp2[i] = max(dp2[i - 1] + dp2[i], dp2[i])
        answer = max(answer, dp1[i], dp2[i])
    
    # 배열의 개수가 1개일때는 위 for문이 돌아가지 않으므로 첫 값의 +-로 결정
    return max(answer, sequence[0], -sequence[0])