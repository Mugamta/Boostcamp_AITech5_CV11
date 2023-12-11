import sys


def func():
    N, M, R = map(int, sys.stdin.readline().split())
    As = list(map(int, sys.stdin.readline().split()))
    Bs = list(map(int, sys.stdin.readline().split()))

    # 두 말뚝을 골라 밑변 개수 구하기 -> 좌표 상 최대 0 ~ 40000
    # 여기서 최대 넓이 R을 초과하지 않는 깃대 구하기 -> 이분탐색 -> O(logM) -> O(log(40000) -> 16이하

    As.sort()
    Bs.sort()

    widths = set()
    for i in range(N):
        for j in range(i+1, N):  # 서로 다른 두 말뚝을 골라 밑변의 후보로 등록
            if As[j] - As[i] <= R:  # 밑변의 후보가 넓이보다 크면 안되므로, 작은 경우만 등록
                widths.add(As[j] - As[i])
            else:
                break

    area_max = 0
    for width in widths:  # 이후 너비를 하나하나 순회하면서
        left, right = 0, M-1

        while left <= right:  # 이분 탐색으로 이 밑변에 대해, R을 초과하지 않는 최대 높이를 구함
            mid = (left + right) // 2

            if width * Bs[mid] / 2 > R:  # R보다 크다면 왼쪽으로 이동
                right = mid - 1

            elif width * Bs[mid] / 2 < R:  # R보다 작다면 오른쪽으로 이동
                left = mid + 1
                area_max = max(area_max, width * Bs[mid] / 2)  # 넓이의 최댓값 갱신

            else:
                # 넓이가 정확히 R인 경우, 더 이상 탐색 불필요
                print("{:.1f}".format(R))
                return

    if area_max == 0:
        print(-1)
    else:
        print("{:.1f}".format(area_max))


func()
