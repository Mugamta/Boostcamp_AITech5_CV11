"""
문제 읽기 1분 소요
순수 구현 시간 40분 소요
s, d 순서로 1시간, 방향 잘못적은거에서 1시간 고민함
"""


def func():
    N, M, K = map(int, input().split())

    fireballs = [list(map(int, input().split())) for _ in range(M)]

    # 8가지 방향
    plus_x = [0, 1, 1, 1, 0, -1, -1, -1]
    plus_y = [-1, -1, 0, 1, 1, 1, 0, -1]

    # 0 ~ N-1 범위를 사용하기 위해 1을 빼줌
    for fireball in fireballs:
        fireball[0] -= 1
        fireball[1] -= 1

    # N x N 격자
    arr = [[[] for _ in range(N)] for _ in range(N)]

    for p in range(K):
        # 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다.
        for fireball in fireballs:
            fireball[0] = (fireball[0] + fireball[3] * plus_y[fireball[4]]) % N
            fireball[1] = (fireball[1] + fireball[3] * plus_x[fireball[4]]) % N
            arr[fireball[0]][fireball[1]].append(fireball)

        fireballs.clear()  # arr에 전달했으므로 초기화

        for i in range(N):
            for j in range(N):
                if len(arr[i][j]) >= 2:  # 2. 2개 이상의 파이어볼이 있는 칸에서는

                    fireball_num = 0
                    fireball_speed_sum = 0
                    fireball_weight_sum = 0
                    fireball_direct_sum = 0

                    # 2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐지고,
                    for fireball in arr[i][j]:
                        fireball_weight_sum += fireball[2]
                        fireball_speed_sum += fireball[3]
                        fireball_num += 1
                        fireball_direct_sum += fireball[4] % 2  # 2-3-3. 홀수의 개수와 짝수의 개수를 더한다

                    # 2-2,3 각 파이어볼은 네 개로 나뉘어지고, 질량은 [sum/5], 속력은 [sum/num]이 된다.
                    small_fireball_weight = fireball_weight_sum // 5
                    if small_fireball_weight > 0:  # 2-4. 질량이 0인 파이어볼은 소멸되어 없어진다.
                        direct = [0, 2, 4, 6]  # 2-3-3. 모두 홀수이거나 짝수이면 방향은 0, 2, 4, 6
                        if 1 <= fireball_direct_sum < fireball_num:
                            direct = [1, 3, 5, 7]  # 아닐 시 1, 3, 5, 7

                        for k in range(4):
                            fireballs.append(
                                [i, j, small_fireball_weight, fireball_speed_sum // fireball_num, direct[k]])

                    arr[i][j].clear()  # fireball에 전달했으므로 초기화

                elif len(arr[i][j]) == 1:
                    fireballs.append(arr[i][j][0])
                    arr[i][j].clear() # fireball에 전달했으므로 초기화

    result = 0
    for fireball in fireballs:
        result += fireball[2]
    print(result)


func()