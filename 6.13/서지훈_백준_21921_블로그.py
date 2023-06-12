N, X = map(int, input().split())
li = list(map(int, input().split()))

start, end = 0, X
max_visit = 0
cnt = 1

for i in range(X):
    max_visit += li[i]
visit = max_visit

while end < N:
    if max_visit < visit + li[end] - li[start]:
        max_visit = visit + li[end] - li[start]
        cnt = 1
    elif max_visit == visit + li[end] - li[start]:
        cnt += 1
    visit = visit + li[end] - li[start]
    start += 1
    end += 1

if max_visit > 0:
    print(max_visit)
    print(cnt)
else:
    print("SAD")