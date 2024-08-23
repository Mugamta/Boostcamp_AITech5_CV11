import sys
input = sys.stdin.readline

def solution(n, arr):
    """
    goal: 카드 n개를 갖기 위해 지불해야 하는 금액의 최솟값 구하기
    how:
        - 다이나믹 프로그래밍
        - dp[i]: 카드 i개를 갖기 위해 지불해야 하는 금액의 최솟값
        - dp[i] = min(dp[i], dp[i - 1] + arr[0], dp[i - 2] + arr[1], ...)
        - 이중 루프를 통해 구현 가능
    """
    dp = [0] + arr

    # 카드 n개를 갖기 위해 지불해야 하는 금액을 순차적으로 계산
    for i in range(1, n + 1):
        # 카드 i개를 가질 수 있는 모든 경우의 수를 비교한 뒤, 최소 금액을 dp에 저장
        for j in range(1, i + 1):
            tmp = dp[i - j] + arr[j - 1]
            if tmp < dp[i]:
                dp[i] = tmp

    return dp[n]


if __name__ == "__main__":
    # 입력
    N = int(input())
    cardpack_info = list(map(int, input().split()))

    # 함수 호출
    res = solution(N, cardpack_info)

    # 결과 출력
    print(res)
