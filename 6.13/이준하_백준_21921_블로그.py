# 슬라이딩 윈도우
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int, input().split()))

# 초기값 설정
max_visit = sum(visited[:X])
cnt = 1

new_visit = max_visit
# 슬라이딩 윈도우
for i in range(X,N):
    new_visit = new_visit + visited[i] - visited[i - X]
    if new_visit > max_visit:
        max_visit = new_visit
        cnt = 1
    elif new_visit == max_visit:
        cnt += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)