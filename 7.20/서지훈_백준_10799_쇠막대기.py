"""
일단 괄호보고 스택문제 생각함
스택문제 맞는거같은데
"""

s = input()
length = len(s)


cnt = 0  # 레이저로 자르면 몇 개의 조각이 남는지 카운팅
res = 0  # 결과값
i = 0  # index

while i < length:
    if s[i] == '(':
        if s[i+1] == ')':  # 레이저인 경우
            res += cnt  # 자르고 결과값에 더함
            i += 1
        else:
            cnt += 1  # 아니면 막대가 하나 늘어난것이므로 cnt 1 증가
    else:
        cnt -= 1  # 막대기가 끝나는 경우에는 값이 1 감소
        res += 1  # 단, 이 막대가 레이저로 이미 잘린 것이므로 결과값에는 1을 더함
    i += 1

print(res)