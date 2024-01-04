# 뒤에 있는 -> 대부분 스택 문제 (대개 우선순위 큐로도 풀 수 있음)
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]  # -1로 초기화해둠
    
    stack = []
    stack_length = 0
    
    for i in range(len(numbers)):
        # 스택이 비어있지 않으며, 스택의 최상단 값(인덱스)이 가르키는 값보다 현재 값이 작다면
        while stack and numbers[stack[stack_length - 1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]  # 스택의 최상단 값의 오큰수는 현재 값이 된다
            stack_length -= 1

        stack.append(i)
        stack_length += 1
            
    return answer