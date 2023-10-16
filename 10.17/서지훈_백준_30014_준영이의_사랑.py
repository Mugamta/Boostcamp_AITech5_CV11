import sys
from collections import deque


def func():
    N = int(input())
    li = list(map(int, input().split()))
    
    # 큰 수끼리 곱하고, 작은 수끼리 곱해야 최종 결과가 가장 커짐
    # 양 끝 수가 서로 곱해지므로, 양 끝 수를 작게 하고 큰 수를 중앙에 배치하는 것이 이득
    
    li.sort(key=lambda x: -x)  # 내림차순 정렬

    dq = deque([li[0]])  # 가장 큰 값 배치

    idx = 1
    while idx < N:
        dq.append(li[idx])  # 이후 큰 값을 순서대로 우측,
        idx += 1

        if idx < N:  # 그리고 좌측에 배치
            dq.appendleft(li[idx])
            idx += 1
    
    # 이 결과로 큰 값은 중앙에 모이고, 작은 값은 양 끝에 모이게 됨

    res = 0
    for i in range(N-1):  # 결과 값 계산
        res += dq[i] * dq[i+1]
    res += dq[N-1] * dq[0]

    print(res)
    for i in dq:
        sys.stdout.write(str(i) + " ")


func()
