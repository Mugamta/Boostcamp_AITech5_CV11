import sys

input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())

maps = []
for _ in range (M):
    line = [f for f in input().strip()]
    maps.append(line)

# 누적합 배열
sum_prefix = {
    'J' : [[0] * (N + 1) for _ in range(M + 1)],
    'O' : [[0] * (N + 1) for _ in range(M + 1)],
    'I' : [[0] * (N + 1) for _ in range(M + 1)],
}

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if maps[i - 1][j - 1]:
            sum_prefix[maps[i - 1][j - 1]][i][j] += 1
        
        for key in sum_prefix.keys():
            sum_prefix[key][i][j] = sum_prefix[key][i][j - 1] + sum_prefix[key][i - 1][j] - sum_prefix[key][i - 1][j - 1] + sum_prefix[key][i][j]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    for key, values in sum_prefix.items():
        if (key != 'I'):
            print(values[c][d] - values[c][b-1] - values[a-1][d] + values[a-1][b-1], end=' ')
        else:
            print(values[c][d] - values[c][b-1] - values[a-1][d] + values[a-1][b-1])
        
