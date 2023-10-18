def func():
    N = int(input())
    S = input()

    # 문자열의 개수는 최대 2000이므로, 최대 귀뚜라미의 수는 2000이다.
    # 주기(1 ~ 2000) x 2000은 400만이므로, O(N^2)으로 시간초과는 나지 않는다.

    res = N+1
    for cycle in range(1, N+1):  # 귀뚜라미가 우는 주기
        tmp_res = 0

        for idx in range(cycle):  # 첫 주기 전 우는 모든 귀뚜라미는 새로운 귀뚜라미
            if S[idx] == '#':
                tmp_res += 1

        for idx in range(cycle, N):  # 이후 어떤 귀뚜라미가 울었을 때, 이전 사이클에 울지 않았다면 새로운 귀뚜라미
            if S[idx] == '#' and S[idx-cycle] != '#':
                tmp_res += 1

        res = min(res, tmp_res)  # 주기마다의 최소 귀뚜라미 수를 저장

    print(res)


func()
