import math


def main():
    N, S = map(int, input().split())
    li = list(map(int, input().split())) + [S]  # 수빈이의 위치를 추가

    li.sort()

    res = abs(li[0] - li[1])

    for i in range(1, N):
        res = math.gcd(res, abs(li[i] - li[i+1]))  # 현재 저장된 값과 다음 간격의 최대공약수

    print(res)


main()