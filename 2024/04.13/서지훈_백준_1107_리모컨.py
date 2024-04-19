"""
문제의 조건 상 O(N^2) 불가능, "최소"
"""


def func():
    # 이동하려고 하는 채널
    N = int(input())

    # 고장난 버튼의 개수
    M = int(input())

    # 0 ~ 9 중, 사용할 수 있는 버튼 체크
    buttons = [True for _ in range(10)]
    if M != 0:
        li = list(map(int, input().split()))
        for button in li:
            buttons[button] = False

    # 채널을 직접 이동하지 않으면 +, -로만 이동이 가능하다.
    # 따라서, 고장나지 않은 버튼을 이용하여 N에 가장 가까운 채널로 이동 후 혹은 채널 100에서, +-로 이동해야 한다.

    # 채널의 개수는 최대 50만이므로, 모든 수를 순회하며 N에 가장 가까운 수를 찾아도 된다. (자릿수는 최대 6이므로, 600만 이하)
    # 단, 채널 100 -> 50만과 50만 <- 999900은 같으므로, 1 ~ 999999까지의 모든 채널을 탐색하자.

    res = 2000000  # 채널 변경에 필요한 버튼 수와 +, -로 조작해야 하는 버튼 수

    for channel in range(1000000):
        # 버튼이 0이 아니거나 0이지만 사용 가능하다면 true 시작, 아니면 false
        flag = True if channel != 0 or buttons[0] else False

        # 채널 변경에 사용된 버튼 수는 0으로 시작하지만, 0이면 while문을 거치지 않으므로 0으로 시작
        tmp = 0 if channel != 0 else 1

        origin = channel
        while channel > 0:

            if not buttons[channel % 10]:
                flag = False
                break

            channel //= 10
            tmp += 1  # 그 값은 숫자의 길이와 같음

        # 채널이 100이면 시작 채널이므로, 버튼을 누르지 않고 도달 가능
        if origin == 100:
            flag = True
            tmp = 0

        # 사용 가능한 버튼만 사용했어야 함
        if not flag:
            continue

        # 현재 채널까지 도달하기 위한 버튼의 횟수 tmp
        # 현재 채널에서 N까지 +, -를 눌러야 하는 값 abs(origin - N)
        if res > tmp + abs(origin - N):
            res = tmp + abs(origin - N)

    print(res)


func()
