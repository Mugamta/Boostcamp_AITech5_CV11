"""
최대값에서 빼는게 이득 아닌가? 라는 생각으로 바로 구현 시작
7분간 첫 코드 작성 - 실패 - 원인은 값을 무시하고 그냥 합계에서 n을 뺀 평균을 내서 계산했기 때문
12분에 코드 수정 - 실패 - 값이 분배되다 만 경우, 마지막에 더해주는 부분이 필요

도중에 우선순위 큐로 해도 시간초과가 나지 않겠다는 (n이 백만 이하이므로) 생각이 들어
해당 코드 5분간 작성 후 성공

30분 후 코드 수정 - 실패 - 값이 고르게 분배된 경우, 마지막에 더해주는 부분의 조건이 n이 아니였음
50분 후 코드 제출 - 성공
"""

def solution(n, works):
    answer = 0
    
    if sum(works) > n:
        works.sort(key=lambda x: -x)  # 내림차순 정렬
        
        cnt = 0  # 가장 큰 값부터 줄여나가며, 같은 값의 개수를 체크
        value = works[0]  # 이때의 값
        
        for work in works:
            if n == 0:
                answer += work ** 2
            
            elif n >= (value - work) * cnt:  # 가장 큰 값들을 현재 work에 맞출수 있는지
                n -= (value - work) * cnt
                value = work
                cnt += 1
                
            else:  # 맞출 수 없다면 일부를 줄이고 계산
                value -= n // cnt
                value_minus1_num = n % cnt  # value-1의 값을 갖는 개수
                value_num = cnt - value_minus1_num  # value
                
                answer += (work ** 2)
                answer += value_num * (value ** 2)
                answer += value_minus1_num * ((value - 1) ** 2)
                cnt = 0
                n = 0
        
        if cnt != 0:
            value -= n // cnt
            value_minus1_num = n % cnt
            value_num = cnt - value_minus1_num
                
            answer += value_num * value ** 2
            answer += value_minus1_num * (value - 1) ** 2
        
    return answer