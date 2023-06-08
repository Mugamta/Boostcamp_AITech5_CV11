def main():
    N, M = map(int, input().split())
    li = sorted(list(map(int, input().split())))
    left = 0
    right = N-1

    result = 0
    while left < right:
        if li[left] + li[right] >= M:
            result += 1
            right -= 1
        left += 1
    print(result)


main()