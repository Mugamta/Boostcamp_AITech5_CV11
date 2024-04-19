import sys

input = sys.stdin.readline

N = int(input())
maps = [tuple(map(int, input().split())) for _ in range(N)]
maps.sort()

result = 0

start, end = maps[0]
for idx in range(1, N):
    a, b = maps[idx]

    # 새로운 시작 좌표가 현재 선분 범위를 넘어 선다면
    # 겹치는 부분이 없음, 따라서 현재 좌표로 길이 +, 새로운 좌표로 초기화
    if (a >= end):
        result += end - start
        start, end = a, b
    else:
        # 새로운 좌표의 끝이 현재의 end 보다 크다면 end 확장
        if (b > end):
            end = b
#마지막 선분길이 계산
result += end - start
print(result)
