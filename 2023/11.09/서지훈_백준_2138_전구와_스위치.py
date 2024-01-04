def func():
    N = int(input())
    now = list(map(int, input()))
    target = list(map(int, input()))

    # 0번 스위치를 누른다 -> 0번 전구의 상태에 따라, 1번 스위치를 누를지 말지가 정해진다.
    # 1번 스위치의 상태가 결정된다 -> 1번 전구의 상태에 따라, 2번 스위치를 누를지 말지가 정해진다...
    # 0번 스위치를 누르는 것으로 시작하는 것과, 0번 스위치를 누르는 것으로 시작하지 않는 방향이 있다.

    # 0번 스위치를 누르는 시작
    res1 = 1
    now_0 = now[:]
    now_0[0] = 1 - now_0[0]
    now_0[1] = 1 - now_0[1]

    for i in range(1, N):
        # i번째 스위치를 누르는 것은 i-1번째 전구의 상태에 따라 결정
        if now_0[i-1] != target[i-1]:
            for j in range(i-1, i+2):
                if j < N:
                    now_0[j] = 1 - now_0[j]
            res1 += 1

    for i in range(N):
        if now_0[i] != target[i]:
            res1 = -1

    # 0번 스위치를 누르지 않는 경우
    res2 = 0
    for i in range(1, N):
        # i번째 스위치를 누르는 것은 i-1번째 전구의 상태에 따라 결정
        if now[i - 1] != target[i - 1]:
            for j in range(i - 1, i + 2):
                if j < N:
                    now[j] = 1 - now[j]
            res2 += 1

    for i in range(N):
        if now[i] != target[i]:
            res2 = -1

    if res1 != -1 and res2 != -1:
        print(min(res1, res2))
    elif res1 != -1:
        print(res1)
    else:
        print(res2)


func()
