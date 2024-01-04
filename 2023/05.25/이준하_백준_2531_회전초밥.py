# 1. 임의의 위치부터 k개의 접시를 연속해서 먹기
# 2. 1번에서 구한 경우에, 쿠폰으로 먹을 수 있는 초밥을 더한다.
# 3. 2번에서 구한 경우의 수 중 가장 많은 경우의 수를 출력한다.
# 30분 시간초과
# 31분 pypy3로 통과
import sys
input = sys.stdin.readline
# n: 접시의 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시의 개수, c: 쿠폰 번호
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
# 연속해서 먹는 수 -1 만큼 뒤에 추가
sushi += sushi[:k-1]


# 1번
def count(start):
    cnt = 0
    sushi_kind = [0] * (d)
    for i in range(start,start+k):
        if sushi_kind[sushi[i]-1] == 0:
            cnt += 1
        sushi_kind[sushi[i]-1] += 1
    return cnt, sushi_kind

# 2번
num = []
for i in range(n):
    cnt, sushi_kind = count(i)
    if sushi_kind[c-1] == 0:
        cnt = cnt + 1
        sushi_kind[c-1] += 1
    num.append(cnt)

print(max(num))

