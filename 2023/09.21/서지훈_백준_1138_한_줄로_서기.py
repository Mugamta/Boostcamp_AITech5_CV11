def func():
    N = int(input())
    li = list(map(int, input().split()))

    answer = [N+1 for _ in range(N)]

    answer[li[0]] = 1
    # print(answer)

    for height in range(1, N):  # 키가 2인 사람부터 순회
        cnt = 0  # 자신보다 키가 작은 사람
        idx = 0
        # print("키가 {}인 사람은 좌측에 자신보다 큰 사람이 {}명 있어야 한다.".format(height+1, li[height]))
        while cnt <= li[height]:
            if answer[idx] > height+1:
                cnt += 1
            idx += 1

        # print("탐색 결과, 키가 {}인 사람은 index {}에 위치해야 한다.".format(height+1, idx-1))
        answer[idx-1] = height+1
        # print(answer)
        # print()
    for i in answer:
        print(i, end=' ')


func()
