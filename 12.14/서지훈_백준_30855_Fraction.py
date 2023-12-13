import math


def transformation(a):
    if a == '(' or a == ')':  # 괄호는 그대로
        return a
    else:
        return int(a)  # 나머지는 int로 변환해서 리턴


def fraction_calculate(whole_number, numerator, denominator):
    # (b / a) / (d / c)를 연산하는 형태
    numerator, denominator = numerator[0] * denominator[1], numerator[1] * denominator[0]
    
    # 더해질 숫자를 (b / a)라고 할 때 이를 numerator / denominator에 더한 결과
    numerator, denominator = whole_number[0] * denominator + whole_number[1] * numerator, \
                             whole_number[1] * denominator

    return numerator, denominator  # 만들어진 분자, 분모 리턴


def func():
    n = int(input())  # python은 리스트로 입력받으면 되므로 쓰지 않아도 무방한 변수
    li = list(map(transformation, input().split()))  # 숫자를 int로 변환해서 리턴하도록 함

    # 괄호가 잘못된 경우를 계산하여 -1 리턴
    bracket = 0
    for i in li:
        if i == '(':
            bracket += 1
        elif i == ')':
            bracket -= 1

    if bracket != 0:
        print(-1)
        return

    stack = []

    for i in li:
        stack.append(i)

        if i == ')':
            stack.pop()
            # 괄호가 닫히는 순간, 하나의 부분(분자 등)이 완성된다.
            
            tmp = []
            while stack and stack[-1] != '(':
                tmp.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()

            # tmp -> 분모, 분자, 더해질 숫자 순으로 저장
            # 즉, 이 값이 3개가 아니라면 잘못된 입력
            if len(tmp) != 3:
                print(-1)
                return

            # 분모가 없다면 1로 만들어준다.
            whole_number = [tmp[2], 1] if type(tmp[2]) != list else [tmp[2][0], tmp[2][1]]  # 더할 숫자
            numerator = [tmp[1], 1] if type(tmp[1]) != list else [tmp[1][0], tmp[1][1]]  # 분자
            denominator = [tmp[0], 1] if type(tmp[0]) != list else [tmp[0][0], tmp[0][1]]  # 분모

            # 분자/분모 계산
            numerator, denominator = fraction_calculate(whole_number, numerator, denominator)

            # 취합된 분자/분모를 스택에 추가
            stack.append([numerator, denominator])

    # len (stack)이 1이 아닌 경우 raise Value Error를 준 결과 에러 발생
    # -> stack에 여러 개의 값이 저장되어 있는 경우가 존재함 -> 예를 들어 1 1이면 문제 발생
    if len(stack) != 1:
        print(-1)  # 따라서 -1을 줌
        return

    stack = stack.pop()  # 최종적으로 스택은 [[분자, 분모]]를 띄고 있으므로 pop으로 벗겨내고

    # 결과는 기약분수여야 하므로, gcd를 이용하여 이를 계산
    print(stack[0] // math.gcd(stack[0], stack[1]), stack[1] // math.gcd(stack[0], stack[1]))


func()
