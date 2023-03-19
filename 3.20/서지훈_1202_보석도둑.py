"""
가방에 보석을 넣는 문제 - 동적 계획법 혹은 그리디 알고리즘일 확률이 높음

가방의 개수가 30만이므로, 그리디 알고리즘일 확률이 높음 - 이를 우선 시도

보석의 최대 가격을 구해야 함 - 보석을 최대 가격 순으로 정렬
이 보석을 어느 가방에 넣어야 할 것인가?
보석의 무게, 가격이 (5, 8), (1, 10), (1, 1)인 경우 무게가 1, 5인 가방에서
(1, 10)인 가방을 최적으로 넣기 위한 선택지...

이 문제에서 가방에는 최대 한 개의 보석만 넣을 수 있음
보석 대신 가방을 정렬...

가방을 무게 순 오름차순 정렬
보석을 가격 순 정렬
보석을 담을 수 있는 가방 탐색 필요...

가방을 무게 순 오름차순 정렬
보석을 무게 순(오름차순), 가격 순(내림차순) 정렬
가방의 무게가 2이고
무게, 가격이 (1, 10), (2, 20)인 경우에서 문제 발생...
가방에 담을 수 없는 무게가 될 때까지 최대값인 보석을 탐색
가방의 무게가 2이고 무게, 가격이 (1, 10), (1, 5), (2, 11), (3, 11)인 경우 무게 2를 초과하는 보석 3까지 최댓값인 11을 담음
즉, 현재 가방의 무게로 담을 수 있는 보석 중 최댓값을 담게 됨

-- 여기까지 8분
코드 작성 12분 - 실패, 마지막 보석 오류로 추정
코드 수정 - 실패

10분간 고민

문제점 발견 - 보석이 (1, 100), (2, 100), (3, 50)이고 가방이 2, 3인 경우
가방 2에서 100짜리 보석을 하나만 선택하게 됨
따라서 이미 지나간 보석을 활용해야 함
이 중 가장 가치가 높은 것을 사용해야 하므로 우선순위 큐 사용
"""

import sys
import heapq


def func():
    N, K = map(int, sys.stdin.readline().split())

    jewels = []
    bags = []

    for i in range(N):
        jewels.append(list(map(int, sys.stdin.readline().split())))

    for i in range(K):
        bags.append(int(sys.stdin.readline()))

    jewels.sort(key=lambda x: (x[0], -x[1]))  # 보석을 무게 순, 가격 순으로 정렬
    bags.sort()  # 가방을 무게 순으로 정렬
    pq = []

    length = len(jewels)
    result = 0
    idx = 0
    for bag in bags:  # 현재 가방의 무게
        while idx < length and jewels[idx][0] <= bag:  # 현재 가방의 무게로 담을 수 있는 보석을 모두 priority queue에 담음
            heapq.heappush(pq, -jewels[idx][1])
            idx += 1

        if len(pq) >= 1:
            result -= heapq.heappop(pq)

        if len(pq) == 0 and idx == length:
            break

    return result


print(func())
