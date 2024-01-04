import sys


def func():
    N = int(input())
    if N == 2:
        print("NO")  # N이 2라면 [1, 2]도 3이 되는 순간이 있고, [2, 1]도 2가 되는 순간이 있다.
        return

    print("YES")
    sys.stdout.write("1 ")  # N = 1이면 [1]만 가능
    if N >= 3:
        sys.stdout.write("3 2 ")  # N = 3일때 [1, 3, 2]만 가능
    
    # 1 ~ N까지의 합은 N(N+1) / 2이다.
    # 이 값은 N = 4 이상이라면 짝수가 되므로 소수가 될 수 없다.
    # 따라서 N = 3까지의 합은 [1, 3, 2]로 만들 수 있고, 이후 N = 4 ~ 5000까지의 매 순간은 소수가 될 수 없다.
    # 따라서 [1, 3, 2, 4, 5, 6, ... N]을 출력하면 답이 된다.
    
    for i in range(4, N + 1):
        sys.stdout.write(str(i) + " ")


func()
