"""
두 수의 합이 0에 가장 가까운 두 수를 찾는 문제이다.

간단히 생각해서, 두 수의 합이 0에 가까우려면 두 수가 양수/음수이며 절댓값이 비슷하거나, 두 수가 양수/음수라면 절댓값이 작아야 한다.

즉, 절댓값을 기준으로 정렬한 후 가까운 두 수의 합 중 0에 가장 가까운 두 값을 찾으면 된다.
"""

def func():
    N = int(input())
    li = list(map(int, input().split()))
    li.sort(key=lambda x: (abs(x), x))  # 절댓값 기준 정렬 후 절댓값이 같으면 오름차순이 되도록 함

    res = [li[0], li[1]]
    min_value = 2000000000
    for i in range(N-1):
        if abs(li[i+1] + li[i]) < min_value:  # 절댓값의 차이가 더 작은(0에 가까운) 쪽으로 갱신
            min_value = abs(li[i+1] + li[i])
            res[0], res[1] = li[i], li[i+1]

            if min_value == 0:  # 용액의 합이 0이면 더 이상 계산 불필요
                break

    res.sort()
    print(res[0], res[1])


func()
