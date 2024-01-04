"""
양수는 최대한 쪼개되, 한 양수보다 작은 음수가 바로 옆에 있으면 합쳐서 음수 구간을 줄임

"""

for _ in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))

    plus = 0
    minus = 0

    prev = 0

    for i in range(N):
        if li[i] == 0:
            pass
        elif li[i] > 0:
            if prev < 0 and prev + li[i] > 0:  # 이전 구간이 음수인데 현재 숫자로 이 구간을 양수로 치환 가능
                minus -= 1  # 이전 음수 구간이 하나 사라지고
                plus += 1  # 양수 구간이 하나 추가됨
                prev = prev + li[i]  # 구간 값 바꿈
            else:
                plus += 1
                prev = li[i]
        else:
            if prev < 0:  # 이전 값이 음수이면 연속된 구간으로 만듦
                prev += li[i]

            elif prev + li[i] <= 0:  # 이전 값이 양수이면 합쳐서 양수가 될 수 있는지 체크
                minus += 1  # 안 된다면 minus 구간 1 증가
                prev = li[i]

            elif prev + li[i] > 0:
                prev = prev + li[i]  # 이전 값과 합쳐서 양수가 될 수 있다면 포함시키고 값 변경
    if plus > minus:
        print("YES")
    else:
        print("NO")