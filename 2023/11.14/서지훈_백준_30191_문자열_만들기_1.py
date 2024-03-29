import sys


def func():
    N = int(input())
    T = input()

    """
    이 문제의 N은 10만이므로, O(N) 혹은 O(NlogN)의 형태로 끝낼 수 있어야 한다.
    이 문제에서 커서를 움직이는 N은 커서를 좌측으로 옮긴다.
    즉, 커서의 위치를 x라고 가정했을 때, S는 SUx, SNN을 입력하면 xSU의 형태가 된다.
    전자의 경우, SSUU와 같은 문자열을 만났을 때, 커서를 좌측으로 움직이면 이전 문자열을 다시 살피는 형태가 된다.
    SUx -> SxU -> SSUxU 또한, 뒤에 문자열이 더 있는 경우, 현재 커서의 위치가 문자열의 끝이 아니므로 문제가 된다.
    
    뒤부터 문자열을 순회한다고 가정하자.
    SU가 나온다면 SNN를 입력하고, US가 나온다면 UNN를 입력한다.
    이렇게 되는 경우 SSUU에서는 SNSNN이 되므로, 문자열의 가장 앞에서 항상 커서가 끝난다.
    따라서 다음 문자열을 계속 순회하는 것에 유리하다.

    이제, SSUU와 같은 특수한 문자열을 생각해보자.
    S가 등장했다면 U가, U가 등장했다면 S로 끝나야 한다.
    
    만약 SSUU와 같은 경우라면?
    U가 등장했다는 것은 앞에서 S가 존재한다는 뜻이므로, 우선 S를 입력한다.
    -> 이로 인하여, 뒤에 U가 존재하는 것은 입력을 완료했다.
    하지만 현재 S를 아직 만나지 못했으므로, S를 만나기 위해 커서를 앞으로 당겨보자. N을 입력한다.
    앞 인덱스로 커서를 옮겨보면 U를 만날 수 있다. 
    마찬가지로 U는 앞에서 S를 만나야 하므로 따라서 S를 입력한다.
    아직 S를 만나지 못했으므로, 마찬가지로 N을 입력한다.
    이제 커서를 다시 당겨보면, S를 만날 수 있다. 따라서 N을 입력한다.
    커서를 다시 당겨보면, S를 만날 수 있다. 따라서 N을 입력한다.
    -> SNSNNN이라는 결과가 나온다. 이는 SUx -> SxU -> SSUxU -> xSSUU라는 결과로,
        커서를 가장 문자열의 가장 앞으로 돌려놓으며, 문자열을 완성시킬 수 있다.
        
    SU와 같이 U 다음 바로 S가 존재하는 경우에도, SNN으로 커서의 위치를 이동하여 문자열을 앞당길 수 있다.
    
    UUUSSS와 같은 경우도, 우선 UN을 입력하고, 다음이 S이므로 UN을 입력하고, 다음이 S이므로 UN을 입력한다.
    이제 U를 만났으니 NNN을 입력하면 UNUNUNNNN이 된다.
    
    """

    print(N // 2 * 3)  # SU는 SNN, US는 UNN로 묶으므로 시행횟수는 3 * N / 2으로 고정된다.
    US = 0  # +는 U의 등장 횟수를, -는 S의 등장 횟수를 의미한다.

    for i in range(N-1, -1, -1):  # 문자열의 가장 끝부터 순회한다.
        if US == 0:  # 현재 U와 S가 모두 짝지어진 상태일 때,
            if T[i] == 'U':
                sys.stdout.write("SN")  # US을 입력한다.
                US += 1  # U가 1회 등장했다.
            else:
                sys.stdout.write("UN")  # SU을 입력한다.
                US -= 1  # S가 1회 등장했다.

        elif US < 0:  # US가 0보다 작다면, S가 x회 등장한 상태이다.
            if T[i] == 'U':  # 따라서 U를 만났다면
                sys.stdout.write("N")  # N으로 커서의 위치만 변경하고,
                US += 1  # SU로 짝지어졌으므로 값을 1 늘린다.
            else:  # S를 다시 만난다면
                sys.stdout.write("UN")  # 또다시 US를 입력해주고
                US -= 1  # S의 등장횟수를 1 늘린다.

        else:  # US가 0보다 큰, U가 x회 등장한 상태이다.
            if T[i] == 'U':  # 따라서 또다시 U를 만났다면
                sys.stdout.write("SN")  # SN으로 끝의 U를 입력해주며
                US += 1  # U의 등장횟수를 1 늘린다.
            else:  # S를 만났다면
                sys.stdout.write("N")  # 커서의 위치만 변경해주고
                US -= 1  # 짝지어졌으므로 U의 등장횟수를 1 늘린다.


func()
