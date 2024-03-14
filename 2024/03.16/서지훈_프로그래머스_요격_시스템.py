"""
https://blog.naver.com/mugamta/223199061569
targets는 50만 -> log(NlogN)이내 해결

그리디 알고리즘
미사일이 끝나는 좌표를 기준으로 정렬
이후 해당 좌표 -1에 요격 미사일 설치 -> 놓치는 미사일이 없게 됨
"""

def solution(targets):
    answer = 0
    
    last = -1
    targets.sort(key=lambda x:x[1])
    
    for target in targets:
        if target[0] < last < target[1]:  # 현재 미사일의 좌표가 이전 격추 좌표에 속한다면 제외
            continue
        
        last = target[1] - 0.5  # 이 미사일의 끝 좌표는 닿지 않으므로, 끝 좌표에서 살짝 앞 좌표를 격추 좌표로 지정
        answer += 1  # 요격 미사일의 개수 1 증가
    
    return answer