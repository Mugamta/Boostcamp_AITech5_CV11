import sys
from collections import defaultdict


def main():
    N, d, k, c = map(int, sys.stdin.readline().split())

    belt = [int(sys.stdin.readline()) for _ in range(N)]
    belt *= 2

    length = len(belt)

    dic = defaultdict(int)
    cnt = 0
    idx = 0
    while cnt < k and idx < length:
        if d != belt[idx]:
            cnt += 1
        dic[belt[idx]] += 1
        idx += 1

    dic[c] += 1
    result = len(dic)

    start = 0
    while result < d and idx < length:
        dic[belt[start]] -= 1
        if dic[belt[start]] <= 0:
            del dic[belt[start]]
        start += 1

        dic[belt[idx]] += 1
        idx += 1

        result = max(result, len(dic))

    dic[c] += 1
    result = max(result, len(dic))

    return result


print(main())