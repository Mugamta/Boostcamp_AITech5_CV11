T = int(input())

for _ in range(T):
    I, n  = map(int, input().split())
    MAX = []
    for _ in range(n):
        num = int(input())
        MAX.append(max(num, abs(num-I)))    ## 각 개미가 탈출할 수 있는 방향 중 먼 거리
    print(I-min(MAX), max(MAX))