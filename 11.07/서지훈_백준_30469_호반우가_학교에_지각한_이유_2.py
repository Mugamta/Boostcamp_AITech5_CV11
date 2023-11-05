import sys


def func():
    A, B, N = map(int, input().split())

    # 수 자체는 소수일 필요가 없지만, 모든 연속된 두 자릿수는 소수여야 한다.
    # A로 시작해서 B로 끝나는 N 자릿수의 이러한 수를 만들기
    # A의 일의 자리로 시작하는 소수, B의 십의 자리로 끝나는 소수

    # A는 소수이므로, A의 일의자리는 1, 3, 7, 9만 가능하다.
    # B는 소수이지만, B의 십의자리는 모든 수가 가능하다. 단, B의 십의 자리가 일의 자리를 사용하는 소수가 존재해야 한다.

    # 따라서, B의 십의 자리가 1, 3, 7, 9가 아니라면 불가능하다.
    if B // 10 not in [1, 3, 7, 9]:
        print(-1)
    else:
        # 이외의 경우, A의 일의 자리인 1, 3, 7, 9에서,
        # 1은 11
        # 3은 31
        # 7은 71
        # 9는 97 -> 71로 이어갈 수 있다.
        # B의 십의 자리인 1, 3, 7, 9에서, 11, 13, 17, 19으로 B로 이어갈 수 있다.

        # 따라서 A의 일의 자리가 9면 7을 한번 출력한 이후 1을 출력하고,
        # 아니면 1만 출력하면 된다.

        if A % 10 == 9:
            sys.stdout.write(str(A))
            sys.stdout.write("7")
            for _ in range(N-5):
                sys.stdout.write("1")
            sys.stdout.write(str(B))
        else:
            sys.stdout.write(str(A))
            for _ in range(N - 4):
                sys.stdout.write("1")
            sys.stdout.write(str(B))


func()
