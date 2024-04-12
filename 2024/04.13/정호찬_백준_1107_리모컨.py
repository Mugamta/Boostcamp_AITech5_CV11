import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

if m:
    not_working = list(map(str, input().split()))
else:
    not_working = list()

min_button = abs(n - 100) #현재 100번에 위치하고 있기 때문에 최대로 + 또는 - 목표 채널로 이동했을때 버튼 누르는 양을 최댓값으로

for num in range(1000001):
    for s_n in str(num):
        if s_n in not_working:
            break
    else:
        min_button = min(min_button, abs(n - num) + len(str(num)))

print(min_button)