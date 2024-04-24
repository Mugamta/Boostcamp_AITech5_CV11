import sys
input = sys.stdin.readline

def solution(n, p):
    """
    goal: 각 사람이 돈을 인출하는데 필요한 시간의 합의 '최솟값' 구하기
    note:
        - 사람들이 '줄을 서는 순서'에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라짐
    how:
        - 정렬
    """
    dp = [0] * (n + 1)

    p.sort()
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + p[i - 1]

    return sum(dp)


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    P = list(map(int, input().split()))

    # 함수 호출
    res = solution(N, P)

    # 결과 출력
    print(res)
