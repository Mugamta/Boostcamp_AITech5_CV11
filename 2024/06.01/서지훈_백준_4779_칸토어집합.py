"""
제약 조건:
N은 0 ~ 12 이하, 알고리즘 유추 불가

키워드:
3등분, 1이면 멈춘다 -> 분할 정복

실제 문제:
1. N이 충분히 작으므로 12까지 미리 계산하기
2. 각 N마다 분할 정복을 통하여 직접 구하기 -> 분할 정복 특성상 재귀를 이용

"""


import sys


# 런타임 전의 전처리 - 메모리 37864 KB, 시간 60 ms
def func1():
    input = sys.stdin.readline

    answer = []
    results = ['-']
    while len(results) <= 12:  # N은 0 ~ 12이므로, 길이가 13까지 만들어야 하낟.
        # 다음 원소는 이전 원소 + 이전 원소의 길이만큼의 공백 + 이전 원소의 형태로 만들어진다.
        tmp = results[-1] + ' ' * len(results[-1]) + results[-1]
        results.append(tmp)

    while True:
        try:
            N = int(input())

            # 이후, 해당 원소의 인덱스를 그대로 출력한다.
            answer.append(''.join(results[N]))

        except:
            break

    print('\n'.join(answer), end='')


# 재귀 (분할정복) - 메모리 37172 KB, 시간 100 ms
def func2():
    input = sys.stdin.readline

    answer = []

    # 문자열의 길이 (탐색/변경해야 할 구간 참조용), 이 문자열의 시작 인덱스, 실제 문자열의 리스트를 입력으로 받음
    def recursion(n, start_idx, result):
        # 구간을 좌측, 중간, 우측으로 나눠서 생각하자.
        # 좌측 구간은 start_idx              ~ start_idx + n // 3 - 1이다.
        # 중간 구간은 start_idx + n // 3     ~ start_idx + 2 * n // 3 - 1이다.
        # 우측 구간은 start_idx + 2 * n // 3 ~ n // 3이다.

        # 1. 좌측은 길이가 3 이상이라면 재귀 탐색이 필요
        if n >= 3:
            recursion(n // 3, start_idx, result)

        # 2. 중간은 모두 공백으로 대체
        for idx in range(n // 3 + start_idx, 2 * n // 3 + start_idx):
            result[idx] = ' '

        # 3. 우측은 길이가 3 이상이라면 재귀 탐색이 필요
        if n >= 3:
            recursion(n // 3, 2 * n // 3 + start_idx, result)

    while True:
        try:
            N = int(input())

            length = 3 ** N
            res = ['-'] * length

            # 길이와 해당 문자열의 시작 인덱스를 전달
            recursion(length, 0, res)

            answer.append(''.join(res))

        except:
            break

    print('\n'.join(answer), end='')


func2()
