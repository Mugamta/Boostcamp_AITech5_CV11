def func():
    N = int(input())
    S = [(input()) for _ in range(N)]

    Suffix_S = dict()  # 모든 접미사의 개수를 셈
    for i in range(N):
        for j in range(len(S[i])):
            if S[i][j:] not in Suffix_S:
                Suffix_S[S[i][j:]] = 1
            else:
                Suffix_S[S[i][j:]] += 1

    cnt = 0
    for value in Suffix_S.values():
        if value % 2 == 1:  # XOR를 취하면, 홀수 번 등장하면 남고, 짝수번 등장하면 사라진다.
            cnt += 1
    print(cnt)


func()