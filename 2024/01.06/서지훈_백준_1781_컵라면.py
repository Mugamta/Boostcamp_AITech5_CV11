import sys


def func():
    N, M = map(int, sys.stdin.readline().split())

    invest = [[0 for _ in range(N + 1)] for _ in range(M + 1)]  # 기업별 투자금액별 이익
    for _ in range(N):
        li = list(map(int, sys.stdin.readline().split()))
        value = li[0]

        for i in range(1, M + 1):  # i번째 기업의 이익은 li[i]
            invest[i][value] = li[i]

    # 한정된 투자금 내에서 가장 높은 이익을 얻기 -> 한정된 가방 무게에서 가장 높은 보석의 가치를 담기 -> 냅색
    # 냅색의 원리 -> 금액이 0 ~ N일때, 1 ~ M번째 물건을 담거나/담지 않을 때의 최대 가치 탐색
    # 이 문제에서는 한 물건만 존재하는 것이 아니라, 한 기업에 여러 개의 투자 값이 존재할 수 있으므로 이를 모두 탐색

    # dp[i][j]는 i번째 기업까지 투자했을 때, 투자금 j로 가능한 최대 가치
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    # 이 문제에서는 각 기업에 투자한 금액도 알아야 하므로, 이를 계산하기 위한 테이블도 별도로 저장해야 한다.
    # 이때, DP를 이용하여 최대 금액을 계산하므로, 이전에 어떤 경로인지 역추적하는 것은 이전의 정보가 남아있어야 한다.
    # 따라서, 각 금액이 갱신될 때, 어떤 회사에 투자해서 갱신되었는지를 확인한다.
    company = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(1, M + 1):  # 1 ~ M번째 기업에 투자했거나/투자하지 않았을 때의 최대 가치 탐색
        for j in range(1, N + 1):  # 금액은 1 ~ N

            # i번째 기업까지 탐색했을 때 투자금 j로 얻을 수 있는 최대 이익은
            # i - 1번째 기업까지의 최대값 (i번째 기업에 투자하지 않는 경우)
            # i - 1번째 기업까지의 최댓값 + 현재 금액 j에서 기업 i의 투자금 w를 뺀 상황에서, i번째 기업의 이익이 추가

            # k = 0일때, dp[i - 1][j]가 dp[i][j]와 자동으로 비교됨 (이전 값)
            # dp[i][j] = max(dp[i][j], dp[i - 1][j])
            for k in range(j + 1):
                # i번째 기업에서 j 이내의 투자 금액이 있다면 해당 이익 비교 필요

                # dp가 갱신될 때, 각 기업에 투자한 금액 또한 기록되야 하므로 max함수 대신, if 분기 사용 필요
                # i - 1번째 기업까지의 최댓값 + 현재 금액 j에서 기업 i의 투자금 w를 뺀 상황에서, i번째 기업의 이익
                tmp = dp[i - 1][j - k] + invest[i][k]

                # i번째 기업에 투자하는 경우가 이득이 더 크다면
                if tmp > dp[i][j]:
                    dp[i][j] = tmp  # 값 갱신
                    company[i][j] = k  # i번째 기업까지 탐색했을 때, 투자금 j는 투자금 k로 갱신되었음

    print(dp[M][N])

    money = N  # 금액
    res = [0 for _ in range(M + 1)]  # 기업별 투자금 저장 용도

    for m in range(M, 0, -1):  # M번 기업부터 역순으로 탐색
        last_invest = company[m][money]  # 마지막으로 투자된 금액

        res[m] = last_invest  # m번 기업에 해당 금액을 투자했으므로 기록
        money -= last_invest  # 투자된 금액만큼 소지금 차감
        m -= 1  # 이전 기업 탐색

    for i in range(1, M + 1):
        sys.stdout.write(str(res[i]) + " ")


func()
