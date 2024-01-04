"""
()는 1일이다.
((), ())는 에러다.
(())는 2일이다.
()()는 1일이다.

)(는 1일이다.
()(, )()는 에러다.
))((는 2일이다.
)()(는 1일이다. (우리는 최소 일수를 세므로 XX가 우선됨)

즉, 최대 일수는 좌괄호와 우괄호의 연속된 개수에 따라 결정된다.
"""


def func():
    N, S = int(input()), input()

    res = 0
    cnt = 0

    for bracket in S:
        # 좌괄호는 1로, 우괄호는 -1로 치환하여 개수 연산
        if bracket == '(':
            cnt += 1
        else:
            cnt -= 1

        res = max(res, abs(cnt))

    if cnt == 0:
        print(res)
    else:  # 좌괄호와 우괄호의 개수가 일치하지 않으면 원하는 문자열 불가능, -1 출력
        print(-1)


func()
