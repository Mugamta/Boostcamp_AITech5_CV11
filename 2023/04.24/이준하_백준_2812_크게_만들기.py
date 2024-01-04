import sys
input=sys.stdin.readline

N, K = map(int, input().split())
length = N - K
num = list(input())
stack = []

for i in num:
    while(K > 0 and stack and stack[-1] < i):
        stack.pop()
        K-=1
    stack.append(i)
    
print(''.join(stack[:length]))