def solution(numbers):
    result = [-1 for _ in range(len(numbers))]      ## -1로 초기화
    stack = []                                      ## 인덱스 저장 스택

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:    # 스택이 비어있지 않고 현재 원소보다 작은 원소가 스택의 가장 위에 있을 경우
            result[stack.pop()] = numbers[i]        ## 뒤 큰수 현재 number로 업데이트
        stack.append(i)                             ## 인덱스를 스택 추가

    return result
