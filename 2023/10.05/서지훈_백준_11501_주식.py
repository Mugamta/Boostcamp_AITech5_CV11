import sys


def func():
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        li = list(map(int, sys.stdin.readline().split()))

        res = 0  # 얻은 총 이익

        # i번째 날에 주식을 사야하는지에 대한 여부는 이후의 날에 더 가격이 높은 날이 있는지에 대한 여부
        # 즉, 현재 값보다 비싼 값이 뒤에 있는지를 판단해야 함

        # 뒤에 있는 가장 큰 주식의 가격을 저장
        max_last = li[N-1]

        # 뒤부터 순회
        for i in range(N-2, -1, -1):

            # 만약 과거의 주식 가격이 더 크다면 그보다 과거의 주식은 과거에 파는 것이 이득
            if li[i] > max_last:
                max_last = li[i]  # 최고값을 갱신

            else:  # 아니라면 현재 최고값에 파는 것이 이득이 됨
                res += max_last - li[i]

        print(res)


func()
