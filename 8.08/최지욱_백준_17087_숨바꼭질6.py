def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    result = abs(arr[0] - S)

    for num in arr[1:]:
        result = get_gcd(result, abs(num - S))

    print(result)

main()