"""
14:57 풀이 시작
13:10 입출력 이해
13:23 자기 자신과 팀인 경우 처리
13:37 방문 가능한 경우
13:50 중단
19:15 재시작
12:24 제출

"""

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = [0]+list(map(int,sys.stdin.readline().split()))
    visit = [False for _ in range(n+1)]
    r = 0
    for i in range(1,n+1):
        if visit[i]:
            continue
        stack = [i]
        d = dict()
        while True:
            visit[stack[-1]] = True
            
            if visit[s[stack[-1]]]:
                if s[stack[-1]] in stack:
                    r += len(stack)-stack.index(s[stack[-1]])
                break
            stack.append(s[stack[-1]])
            
    print(n-r)
