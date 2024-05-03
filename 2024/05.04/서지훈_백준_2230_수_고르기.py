"""
제한조건:
N은 최대 10만 -> O(NlogN) 이내 해결
M은 최대 20억 -> O(logM)으로 사용
-> 그리디 알고리즘, 이분탐색

문제 키워드:
두 수를 골랐을 때 -> 투 포인터

종합:
O(NlogN)으로 해결할 수 있으며, M의 값은 O(logM)으로 해결할 수 있는 경우
투 포인터로 두 값을 탐색하며, 필요한 경우 이분탐색을 사용

실제 문제 분석:
두 수를 골랐을 때, 그 차이가 M 이상이면서 가장 작은 경우 구하기
a과 M 이상 차이나는 수는 M + a 이상인 경우만 탐색
이보다 큰 값인 b의 경우, a에서 찾은 수보다 작은 경우는 탐색할 필요가 없음
따라서 투 포인터 문제가 되며, 따라서 정렬이 필수적임. 즉 정렬 + 투 포인터

메모리: 35364 KB
시간:  120 ms
제출: Python3
"""
import sys


def func():
    N, M = map(int, sys.stdin.readline().split())

    if M == 0:  # M == 0이면 같은 수를 고르면 바로 끝남
        print(0)
        return

    A = [int(sys.stdin.readline()) for _ in range(N)]  # 입력이 많으므로 sys 모듈 사용

    A.sort()  # 투 포인터의 이용을 위하여 정렬하기

    left = 0
    right = 1

    # 첫 번째 값과 M 이상 차이나는 구간까지 right를 옮김
    while A[right] - A[left] < M:
        right += 1

    res = 2000000000  # M 이상인, 가장 작은 차이

    while right < N:  # 문제 특성 상 left가 right보다 커질 일은 없음

        diff = A[right] - A[left]

        if diff >= M:  # M 이상인 값이라면 탐색 완료
            if res > diff:  # res값 갱신
                res = diff

            left += 1  # 다음 수로 변경

        elif diff < M:  # M 이상 차이나지 않으면
            right += 1  # 더 큰 수와 비교 필요

        if res == M:  # M 이하로는 줄어들 수 없음
            print(M)
            return

    print(res)
    return


func()
