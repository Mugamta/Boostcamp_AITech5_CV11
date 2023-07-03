import sys

W, N = map(int, sys.stdin.readline().split(' '))

bag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag.sort(key=lambda x : -x[1])
total = 0

for (weight, price) in bag:
    total += min(W,weight)*price
    W -= min(W,weight)
    if W==0:
        break

print(total)