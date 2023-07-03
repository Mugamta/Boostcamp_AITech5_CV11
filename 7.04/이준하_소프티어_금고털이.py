import sys
input = sys.stdin.readline

W, N = map(int,input().split(' '))

s = [list(map(int, input().split())) for _ in range(N)]

s.sort(key = lambda x : x[1], reverse = True)

B = 0
P = 0
for m,v in s:
    if B+m >= W:
        P += (W-B)*v
        break
    B += m
    P += m*v
print(P)

'''
시간 초과 됨

import sys
input = sys.stdin.readline

W, N = map(int,input().split(' '))

s = [list(map(int, input().split())) for _ in range(N)]

s.sort(key = lambda x : x[1], reverse = True)

B = 0
P = 0
while s:
    m,v = s.pop(0) # pop() 은 O(1), pop(0) 은 O(N) -> 역순으로 하면 될 수도?
    if B+m >= W:
        P += (W-B)*v
        break
    B += m
    P += m*v

print(P)

# https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84
'''
