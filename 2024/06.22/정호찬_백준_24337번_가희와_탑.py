"""
    메모리 : 36540 kb
    시  간 : 108 ms
"""

import sys
input = sys.stdin.readline


# N을 고려하지 않고 필수로 구해야하는 건물순서
def essential_budlings(a, b):
    stack = []

    for h in range(1, a):
        stack.append(h)
    stack.append(max(a, b))
    for h in range(b-1, 0, -1):
        stack.append(h)
    return (stack, len(stack))

N, a, b = map(int, input().split())
e_b, len_e_b = essential_budlings(a, b)

# 만약 필수로 구해야하는 건물이의 조합 수가 N보다 크다면 -1
if len_e_b > N:
    print(-1)
else:
    # 문제에서 핵심은 `사전 순으로 앞임`
    # 따라서 가능한 가장 왼쪽에 1로 채우는것

    # case 1 : a = 1인 경우 시작높이 건물이 왼쪽에서 가장 높은건물
    # case 2 : a > 1인 겨우 시작높이는 무조건 1인 경우
    # 결론적으로 필수 조합 첫번째 요소 다음에 1이 N-len_e_b 개만큼 오면된다.
    print(e_b[0], end=" ")
    for _ in range(N-len_e_b):
        print(1, end=" ")
    print(*e_b[1:])
