import sys

N, M = map(int, sys.stdin.readline().split())
keyword = dict()
for _ in range(N) : #N개의 키워드
    keyword[input()] = 1

answer = N
# keys= keyword.keys()
for _ in range(M) :
    tags = list(sys.stdin.readline().rstrip().split(','))
    for t in tags  :
        if t in keyword.keys() :
            if keyword[t] == 1 :
                keyword[t] = 0
                answer -= 1
    print(answer)

