def solution(p):
    if p=='': 
        return p
    r=True
    c=0
    for i in range(len(p)):
        if p[i]=='(': 
            c-=1
        else: 
            c+=1
        if c>0: 
            r=False
        if c==0: # 균형잡힌 괄호
            if r: # 올바른 괄호
                return p[:i+1]+solution(p[i+1:]) #올바른 부분 + 올바라진 부분
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i])))
            # 올바른 괄호가 아니라면, '(' + 올바라진 부분 + ')' + 나머지 문자열의 괄호 방향을 뒤집은 문자열
solution("()))((()")