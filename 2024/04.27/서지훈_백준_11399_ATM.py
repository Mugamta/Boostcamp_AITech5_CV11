"""
조건:
N, P가 1000 이하 -> O(N^2), O(NP)등이 가능하지만, 문제의 난이도가 쉽기 때문일 수 있음

키워드:
시간 -> 정렬
최솟값 -> DP, BFS, 그리디 등

실제 문제 -> 돈을 인출하는데 걸리는 시간을 적절히 조율하여 시간의 최솟값 만들기
앞의 사람의 시간이 뒤의 사람에 추가되므로, 시간이 많이 걸리는 사람은 앞에 배치하지 않는 것이 좋다.
따라서, 시간이 적게 걸리는 사람의 순서대로 앞에 배치한다.

즉, 정렬 + 작은 사람부터 시간을 사용하는 그리디 알고리즘이다.
"""


def func():
    N = int(input())
    P = list(map(int, input().split()))

    P.sort()  # 시간 순으로 정렬한다.

    res = 0  # 걸리는 총 시간
    last_time = 0  # 이전 사람이 걸린 시간 (현재 사람도 이 만큼의 시간을 사용하므로

    for time in P:
        res += last_time + time  # 이전 사람까지 걸린 시간 + 현재 사람이 출금하는 시간
        last_time += time  # 이전 사람이 걸린 시간 갱신

    print(res)


def func2():
    N = int(input())
    P = list(map(int, input().split()))

    P.sort()  # 시간 순으로 정렬한다.

    res = 0  # 걸리는 총 시간

    # 첫 번째 시간은 N명이, 두 번째 시간은 N -1명...에게 각각 소모된다.
    for time in P:
        res += time * N
        N -= 1

    print(res)


func2()
