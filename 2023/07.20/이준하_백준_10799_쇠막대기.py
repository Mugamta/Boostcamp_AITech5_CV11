import sys
input = sys.stdin.readline

razor = list(input())
answer = 0
st = []

for i in range(len(razor)):
    #'('는 그냥 스택에 append
    if razor[i] == '(':
        st.append('(')
    else:
        # ')'가 나오고 이전 문자가 '('면, 레이저이므로 스택에서 '('를 pop하고, 스택의 길이만큼 answer에 더함
        if razor[i-1] == '(': 
            st.pop()
            answer += len(st)
        # ')'가 나오고 이전 문자가 ')'면, 막대기의 끝이므로 스택에서 '('를 pop하고, answer에 1을 더함
        else:
            st.pop() 
            answer += 1 
print(answer)