import sys
from heapq import heappush, heappop


def func():
    N = int(input())

    # 최소의 강의실을 이용하여 모든 수업을 가능하게 해야 함
    # 1. N이 20만이므로 그리디 알고리즘일 확률이 높음.
    # 2. S에 시작하여 T에 끝나는 수업 -> 시간 순으로 정렬 필요
    # 3. S ~ T의 시간을 채워넣어 구간을 카운팅 하면 가능, 하지만 값이 최대 10^9이므로 시간초과 발생
    # 4.  정렬 + 카운팅이 가능 -> 우선순위 큐

    lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    pq = []

    # 그리디 알고리즘의 형태이므로, 시작 혹은 종료 시간을 기준으로 정렬
    # 각 수업이 종료된 후에 새로운 강의실을 사용할 수 있으므로 (더 적은 강의실을 사용) 종료 시간을 기준으로 정렬
    # 1 2 3
    #   2 3 4
    #     3 4 5
    # 가령 위 형태에서 겹치는 시간대는 3이며, 이는 종료 시간이다.

    # 시작 시간이 빠른 강의를 기준으로 정렬
    lectures.sort(key=lambda x: x[0])

    # 첫 번째 강의를 우선 우선순위 큐에 넣음
    heappush(pq, lectures[0][1])

    cnt = 1  # 필요한 강의실의 개수

    # 이제 나머지 강의를 순회
    for i in range(1, N):

        # 현재 강의의 시작 시간과 현재 강의실의 종료 시간을 비교
        if lectures[i][0] < pq[0]:  # 종료 시간이 더 늦다면, 추가로 강의실이 필요함
            heappush(pq, lectures[i][1])  # 따라서 이 강의는 추가 강의실에 배정
            cnt += 1  # 이 경우 필요한 강의실의 개수가 늘어남

        else:
            # 종료시간이 같거나 더 빠르다면
            heappop(pq)  # 현재 강의는 이 강의실에서 수강 가능, 저장된 강의 삭제
            heappush(pq, lectures[i][1])  # 이후 현재 강의를 넣음

    # 마지막 강의가 종료되었으므로, 아직 종료되지 않은 (강의

    print(cnt)


func()
