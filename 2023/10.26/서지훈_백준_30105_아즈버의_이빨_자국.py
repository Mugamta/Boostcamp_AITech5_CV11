import sys


def func():
    N = int(input())
    marks = list(map(int, input().split()))

    # 모든 간격을 조사하면 O(N^2)
    # 간격은 모든 경우를 만족시켜야 하므로, 첫 송곳니와 다른 송곳니만 조사하면 O(N)
    # 첫 번째 송곳니와 중간을 넘어가는 송곳니의 간격으로는 모든 송곳니를 만족시킬 수 없음
    # 가령 0, 15, 30, 45, 60

    # 첫 번째 송곳니와 중간까지의 송곳니의 간격을 계산
    # intervals = [marks[i] - marks[0] for i in range(1, N // 2 + 2)]

    # 첫 번째 송곳니와 모든 송곳니의 간격을 계산
    intervals = [marks[i] - marks[0] for i in range(1, N // 2 + 1)]

    # print(intervals)

    marks_s = set(marks)

    answer = []
    for interval in intervals:
        able = True
        for i in range(N):
            # 이 이빨자국에서 간격만큼 떨어진 곳에 이빨자국이 있는지
            if not marks[i] - interval in marks_s and not marks[i] + interval in marks_s:
                able = False
                break

        if able:
            answer.append(interval)

    if len(answer) != 0:
        sys.stdout.write(str(len(answer)) + "\n")
        for i in answer:
            sys.stdout.write(str(i) + " ")
    else:
        sys.stdout.write("0")


func()