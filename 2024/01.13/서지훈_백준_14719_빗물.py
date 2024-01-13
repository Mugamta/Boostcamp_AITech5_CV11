def func():
    H, W = map(int, input().split())
    Hs = list(map(int, input().split()))

    # 500, 0, 0, 0, ... , 0, 500이라고 가정했을 때,
    # 488개 범위를 총 500개 쌓아올려도 500 x 500으로 250000번의 연산 -> 시뮬레이션으로 시간초과 발생하지 않음

    blocks = [[False for _ in range(W)] for _ in range(H + 1)]
    for x in range(W):
        for y in range(Hs[x] + 1):
            blocks[y][x] = True

    res = 0
    for height in range(H + 1):  # 높이는 0 ~ H의 범위 조사

        # 좌측 - 우측 범위를 조사하여 가운데에 물을 채워야 함
        left, right = -1, -1
        for width in range(W):

            # 물이 차 있는 좌측/우측 지점을 찾음
            if left == -1 and blocks[height][width]:
                left = width

            # 좌측/우측이 동시에 갱신되지 않도록 if - elif를 사용
            elif right == -1 and blocks[height][width]:
                right = width

            # 만약 좌측/우측 지점을 찾았다면 해당 범위에서 물이 차는 곳을 탐색
            if left != -1 and right != -1:
                for i in range(left, right + 1):

                    if not blocks[height][i]:  # 물이 찬 범위가 아니라면
                        res += 1  # 물이 고이므로 1 증가

                # 우측은 좌측 값으로 초기화하기
                left, right = right, -1

    print(res)


func()
