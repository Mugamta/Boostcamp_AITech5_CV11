import sys

W, N = map(int, sys.stdin.readline().split())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li.sort(key=lambda x : -x[1])

idx = 0
res = 0
while W > 0 and idx < len(li):
    if W < li[idx][0]: # 현재 배낭의 남은 무게보다 보석이 더 큰 경우
        res += W * li[idx][1] # 현재 배낭에 담을 수 있는 만큼 잘라서 가져감
        break
    else:
        W -= li[idx][0] # 배낭에 현재 보석의 무게를 담고
        res += li[idx][0] * li[idx][1] # 결과에 무게 * 무게당 가격을 더함
    idx += 1
print(res)