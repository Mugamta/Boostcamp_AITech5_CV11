"""
어디서 본 문제 -> 괄호면 스택?

문자열은 균형잡힌 괄호 문자열 u, v로 분리 -> u는 더 이상 분리 불가능해야함 -> 분할 정복?

문제 자체는 구현의 형태를 이룸... p는 최대 1000이므로 O(N^2)을 해도 시간초과 안남 -> 브루트 포스 형태?

func()
1. 문자열을 좌측부터 순회하여 (와 )의 개수가 같아질때까지 u를 만들어냄
2. u가 올바른 괄호 문자열이라면 u에 func(v)를 이어붙임
3. 올바른 괄호 문자열이 아니라면 (와 문자열 v를 1부터 실행한 결과를 이어붙이고, )를 붙이고, u의 첫번째, 마지막을 제거하고 괄호 뒤집고 v 뒤에 붙이고 반환

"""
def check(u):
    stack = []
    length = 0
    for ele in u:
        if ele == '(':
            stack.append(ele)
            length += 1
        else:  # )
            if length == 0:
                return False
            elif stack[length-1] == '(':
                stack.pop()
                length -= 1
    return True
            
def func(w):
    # 1. 입력이 빈 문자열인 경우 그대로 반환
    if len(w) == 0:
        return ''
    
    left = 0
    right = 0
    idx = 0
    while idx < len(w) and (left != right or left + right == 0):
        if w[idx] == '(':
            left += 1
        elif w[idx] == ')':
            right += 1
        idx += 1

    # 2. 문자열 w를 분리
    u = w[:idx]
    v = w[idx:]
    
    if left != right:
        u = ""
        v = w
    
    # 3. 문자열 u가 올바른 괄호 문자열인지 검사
    if check(u) == True:
        return u + func(v)  # 4. 올바르면 v를 수행한 결과에 이어붙인 후 반환
    else:
        s = ''
        for i in u[1:len(u)-1]:
            if i == '(':
                s += ')'
            else:
                s += '('
        return '(' + func(v) + ')' + s

def solution(p):
    return func(p)