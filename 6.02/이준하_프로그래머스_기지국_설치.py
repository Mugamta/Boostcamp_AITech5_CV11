from math import ceil

def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1
    
    start = 1
    # 기지국이 설치된 곳을 기준으로 전파가 닿지 않는 곳을 계산
    for s in stations:
        answer += max(ceil((s - w - start) / W), 0)
        start = s + w + 1

    # 마지막 기지국 이후에도 전파가 닿지 않는 곳을 계산
    if n >= start:
        answer += ceil((n - start + 1) / W)
    
    return answer

6.02\이준하_프로그래머스_기지국_설치.py