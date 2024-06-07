"""
조건:
O(NlogN) 이내 해결

키워드:
힙, 자료구조

-> 특수한 자료구조 구현 문제
"""


from sys import stdin
from heapq import heappush, heappop


def func():
    input = stdin.readline

    answer = []

    hq = []
    N = int(input())
    for _ in range(N):
        x = int(input())

        if x == 0:
            answer.append(heappop(hq)[1] if hq else 0)  # 큐가 비어있지 않다면 원본 수를, 아니면 0을 출력
        else:
            heappush(hq, (abs(x), x))  # 절댓값과 일반 값을 모두 저장하기 (절댓값이 작은 값 이후 작은 값 순서)

    print('\n'.join(map(str, answer)), end='')


func()
