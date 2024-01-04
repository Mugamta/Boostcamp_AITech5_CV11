def func():
    N = int(input())
    li = list(map(int, input().split()))

    if N == 1:
        print(li[0], 1)
        return

    # 1 <= i <= j <= N인 두 수 i, j에 대하여 a[i] = a[j]라면,
    # 합은 a[i] ~ a[j]까지의 합...

    # a[i] = a[j]인 두 수의 위치를 찾기...
    # a[x]와 x를 묶어 (a[x], x)의 형태의 리스트를 만들고
    # 이 리스트를 a[x]를 기준으로 정렬한 후, 같은 a[x]들의 위치를 찾는다.
    # 이때 같은 a[x]에 대해서, i, j, k...가 있다면 당연히 i와 k가 가장 큰 값이다.
    # 따라서 하나씩만 고른다.
    li2 = [[li[i], i] for i in range(N)]
    li2.sort(key=lambda x: (x[0], x[1]))

    # 이때 이러한 합의 최대값을 찾고, 이 값이 몇개인지 구하기
    # 합을 구하기 -> 누적합을 이용하기

    max_sum = 0
    max_sum_cnt = 0

    d = dict()
    for i in range(N):
        if li2[i][0] not in d:
            d[li2[i][0]] = (li2[i][1], li2[i][1])
        else:
            d[li2[i][0]] = (d[li2[i][0]][0], li2[i][1])

    prefix_sum = [0 for _ in range(N)]
    prefix_sum[0] = li[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + li[i]

    max_sum = 0
    max_sum_cnt = 1

    for key in d.keys():
        start_idx, end_idx = d[key][0], d[key][1]
        tmp_sum = prefix_sum[end_idx] - (prefix_sum[start_idx - 1] if start_idx >= 1 else 0)

        if max_sum < tmp_sum:
            max_sum = tmp_sum
            max_sum_cnt = 1
        elif max_sum == tmp_sum:
            max_sum_cnt += 1

    print(max_sum, max_sum_cnt)


func()
