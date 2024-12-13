import sys
from collections import deque
input = sys.stdin.readline

def solution(n, arr):
    cnt = 0

    arr.sort(key=lambda x: (x[1], x[0]))
    arr = deque(arr)
    prev_end = -1

    while arr:
        start, end = arr.popleft()
        if start >= prev_end:
            prev_end = end
            cnt += 1

    return cnt

def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solution(N, arr)

    print(res)


if __name__ == "__main__":
    main()
