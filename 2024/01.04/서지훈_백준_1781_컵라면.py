import sys
from heapq import heappop, heappush


def func():
    N = int(sys.stdin.readline())
    li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    li.sort(key=lambda x: (x[0], -x[1]))

    # N이 20만이므로, O(NlogN) 이내에 해결 가능해야 함
    # 그리디, 이분탐색, 정렬 등의 방법을 떠올릴 수 있음

    # 1. 문제에서 요구하는 것은 최대 컵라면 수이므로, 그리디 알고리즘/DP 등의 키워드를 생각할 수 있다.
    # 2. 최대 컵라면을 얻으려면, 같은 데드라인이라면 컵라면이 많은 문제를 우선해서 풀어야 한다. -> 정렬, 우선순위 큐
    # 데드라인이 2일때 받을 수 있는 컵라면이 5, 6이라도 데드라인 3에 컵라면 7, 8, 9가 있다면 해당 컵라면이 우선됨
    # -> 데드라인보다 컵라면의 개수가 우선순위가 되거나, 이미 담은 값을 바꿔주어야 함 -> 우선순위 큐

    pq = []  # 선택할 문제
    time = 1  # 시간
    for i in range(N):
        deadline, cup_ramen = li[i]

        # 현재 데이터가 타임라인에 걸리지 않는다면
        if time <= deadline:
            heappush(pq, cup_ramen)  # 문제를 해결하고 컵라면을 받아감
            time += 1  # 시간 증가

        # 현재 데이터가 데드라인에 걸리지만,
        # 힙의 최상단 값인 가장 작은 컵라면보다 현재 컵라면 개수가 더 많다면
        elif time > deadline and pq[0] < cup_ramen:
            heappop(pq)  # 해당 문제를 푸는 대신
            heappush(pq, cup_ramen)  # 이 문제를 푸는 것이 이득
            # 푼 문제 수는 그대로이므로 시간은 그대로 둠

    res = sum(pq)
    print(res)


func()
