"""
분할정복
"""
def solve(n):
    if (n == 1):
        return ("-")
    inner = " " * (n // 3)
    outter = solve(n // 3)
    return (outter + inner + outter)

while (1):
    try:
        N = int(input())
        print(solve(3**N))

    except:
        break