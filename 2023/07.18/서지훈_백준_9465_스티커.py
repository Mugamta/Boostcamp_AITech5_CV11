"""
결국 대각선으로만 선택 가능
예제는 두 칸 대각선을 이동함
세 칸 대각선은 한 칸, 한 칸을 이동하는것이 더 이득
따라서 한 칸/두 칸 대각선으로 이동하는 방향으로 계산
"""

for _ in range(int(input())):
    n = int(input())
    li1 = [0] + list(map(int, input().split()))
    li2 = [0] + list(map(int, input().split()))

    dp1 = [0 for _ in range(n+1)]
    dp2 = [0 for _ in range(n+1)]

    dp1[1] = li1[1]
    dp2[1] = li2[1]

    for i in range(2, n+1):
        dp1[i] = max(dp2[i-1], dp2[i-2]) + li1[i]  # 윗줄은 왼쪽 대각선 아래 한칸/두칸에서 현재 칸을 더한 것
        dp2[i] = max(dp1[i-1], dp1[i-2]) + li2[i]  # 아랫줄은 왼쪽 대각선 위 한칸/두칸에서 현재 칸을 더한 것

    print(max(dp1[n], dp2[n]))