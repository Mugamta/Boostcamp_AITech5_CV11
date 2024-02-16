def func():
    H, W = map(int, input().split())
    R, C, D = map(int, input().split())

    A = [list(map(int, list(input()))) for _ in range(H)]
    B = [list(map(int, list(input()))) for _ in range(H)]

    dusts = [[True for _ in range(W)] for _ in range(H)]

    plus_C = [0, 1, 0, -1]
    plus_R = [-1, 0, 1, 0]

    res = 0
    cnt = 0
    # print(R, C, D)
    while True:
        if dusts[R][C]:
            dusts[R][C] = False

            D = (D + A[R][C]) % 4
            R, C = R + plus_R[D], C + plus_C[D]

            # 먼지를 제거한 후 다음 칸이 벗어나는 칸이라면
            if not (0 <= R < H and 0 <= C < W):
                res += cnt + 1  # 누적 이동횟수 + 칸을 벗어나는 이동으로 종료
                break

            if cnt > 4 * H * W:  # 이동횟수가 H * W를 훨씬 넘는다면 무의미한 이동 반복중
                break

            res += cnt + 1  # 먼지를 제거했다면 한 칸 이동하여 누적 이동 횟수와 더함
            cnt = 0  # 누적 이동 횟수 초기화

        else:
            D = (D + B[R][C]) % 4
            R, C = R + plus_R[D], C + plus_C[D]

            # 먼지를 제거하지 못하고 영역 밖으로 나갔다면 의미 없는 이동이므로 횟수 더하지 않음
            if not (0 <= R < H and 0 <= C < W) or cnt > 4 * H * W:
                break

            cnt += 1  # 먼지를 제거하지 않았다면 의미 없는 행동을 반복할 수 있으므로 누적횟수로 더해놓음

        # print(R, C, D, " -> ", cnt, res)

    print(res, end='')


func()
