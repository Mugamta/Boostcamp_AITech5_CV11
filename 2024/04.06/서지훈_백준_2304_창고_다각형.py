def func():
    # 기둥의 개수를 나타내는 N
    N = int(input())

    # 면적이 가장 작게 하기 - 단, 오목한 부분이 없어야 함
    # 따라서 어떤 두 높이 h1, h2 사이에는 h1, h2보다 작은 높이가 존재해서는 안된다.
    # 때문에 가장 높은 높이까지는 계속해서 높이를 유지하거나 상승시켜야 한다.
    # 이후에는 가장 높은 높이까지 유지하고, 그 다음 높이로 이동하고...를 반복한다.

    # 가장 높이 이후부터는 뒤에서 가장 높은 높이를 계속해서 찾아야 한다 -> 스택
    # 피크 이후부터의 높이를 스택에 저장
    # [4, 6, 8]이라면 가장 높은 우측 높이가 먼저 나오며, 이보다 높은 것이 없으므로 우측부터 피크까지 갱신
    # [4, 8, 6]이라면 6으로 먼저 갱신되고, 이후 4 구간은 8로 갱신
    # [8, 6, 4]라면 4, 6, 8으록 구간이 차례대로 갱신

    heights = [list(map(int, input().split())) for _ in range(N)]
    heights.sort(key=lambda x: x[0])  # x축을 기준으로 정렬

    # 피크의 시작 높이, 끝 높이를 구함
    max_H, start_idx, end_idx = 0, 0, 0
    for i, (L, H) in enumerate(heights):
        if max_H < H:
            max_H = H
            start_idx = i
            end_idx = i
        elif max_H == H:
            end_idx = i

    res = 0
    last_L, last_H = heights[0][0], heights[0][1]
    # 가장 높은 높이까지는 이전 기둥(높이)의 높이를 따라가는 것이 유리
    for i in range(1, start_idx):
        L, H = heights[i][0], heights[i][1]

        res += last_H * (L - last_L)

        last_L, last_H = L, max(last_H, H)

    # 마지막 구간의 x좌표 ~ 피크들의 x좌표로 피크 이전까지의 넓이를 구함
    res += last_H * (heights[start_idx][0] - last_L)

    # 이제 피크들의 넓이를 구함
    res += max_H * (heights[end_idx][0] - heights[start_idx][0] + 1)

    # 이제 피크 이후의 넓이를 구해야하지만, 굳이 스택을 이용할 필요는 없음
    # 그냥 마지막 높이 중 가장 큰 높이를 이용하면 되므로 값 하나만 이용해도 됨

    last_L, last_H = heights[N - 1][0], heights[N - 1][1]
    for i in range(N - 2, end_idx, -1):
        L, H = heights[i][0], heights[i][1]

        res += last_H * (last_L - L)
        last_H = max(last_H, H)

        last_L = L

    # 피크의 끝 - 마지막 구간 사이의 넓이를 더함
    res += (last_L - heights[end_idx][0]) * last_H

    print(res)


func()
