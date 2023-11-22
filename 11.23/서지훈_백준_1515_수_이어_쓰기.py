def func():
    num = input()

    # 1 ~ N까지의 모든 수를 "차례대로" 쓴 입력에서 일부분이 지워짐 -> 이때 N외 최솟값
    # 문자열은 최대 3천자리이지만, N이 얼마인지 알 수 없음...
    # 15000까지만 순회해도 0 ~ 9의 숫자가 3천번 이상 등장함
    # -> N을 이용한 브루트 포스로 풀 수 있으나, N^2이 되어서는 안됨...
    # O(N^2)은 1억번이 넘으며, 15000 * 3000이 가장 큰 값
    # -> 이는 O(N * len(num)) 이므로, 문자열을 한 번 순회하며 N을 모두 시도하는 브루트 포스 가능

    # 최소가 되는 N을 찾아야 함 -> 문자열의 각 숫자를 순회할 때, N이 최소가 되도록 1 ~ N을 찾아야 함

    # 233 = N
    # 332 -> 매칭 불가
    #  332 -> 33 매칭 가능 -> (233)2

    # 234 = N
    # 235의 경우라면?
    # -> 23(4) -> 235로 이동하면 된다.

    # 즉, 앞의 숫자부터 하나씩 매칭되는지 확인하고, 매칭된다면 입력값의 다음 인덱스로 이동한다.
    # for문은 N의 각 자릿수에 대해서 순회하며 문자열이 가르키는 부분과 자릿수가 일치한다면 num의 인덱스를 증가시킨다.
    # 이 인덱스는 num 전체를 순회해야 하므로, while문에서 index를 순회하며, 내부에 N에 대한 for문을 만든다.

    N = 1
    idx = 0

    length = len(num)
    while idx < length:
        for digit in str(N):  # N의 각 자릿수에 대해서 순회하며
            if num[idx] == digit:  # 값이 일치하면 여기에 N을 사용할 수 있으므로
                idx += 1  # num[idx]는 사용할 수 있게 되며, 따라서 idx를 1 증가시킨다.

                if idx >= length:  # 문자열 범위를 벗어나면 종료
                    print(N)
                    return

        N += 1
    print(N - 1)


func()
