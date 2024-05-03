"""
제한조건:
100 이하의 양수 -> O(N^2) 가능

문제 키워드:
스위치 -> 비트 연산
배수 -> 소수 판정법

종합:
묶이는 정보가 없으므로, 쉬운 문제/브루트 포스/구현/시뮬레이션 등 정해가 없는 문제일 것

실제 문제 분석:
남학생은 자신의 수의 배수인 스위치 번호를 반대로 바꾼다.
여학생은 자신이 받은 수와 같은 번호가 붙은 스위치를 중심으로, 좌우 대칭으로 가장 넓은 구간을 찾아 그 구간을 바꾼다.
즉, 구현 + 시뮬레이션 형태의 문제이다.

틀린 이유:
"스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다."라는 조건 누락으로 출력 형식 오류
여학생의 넓이 탐색을 for문으로 하였는데, N // 2로 조건을 설정하여 틀림 (절반까지 가능하며 잘못될때 반전하므로 + 2 필요)

메모리: 31120 KB
시간: 44ms
제출: Python3
"""


def func():
    N = int(input())
    switch = list(map(int, input().split()))

    for _ in range(int(input())):
        gender, number = map(int, input().split())

        if gender == 1:  # 남학생이라면
            for i in range(number, N + 1, number):  # 번호의 배수인 지점을 찾아서
                switch[i - 1] = 1 - switch[i - 1]  # 상태를 바꿈
        else:  # 여학생이라면
            number -= 1
            for i in range(N // 2 + 2):  # 절반보다 넓은 값을 가질 수는 없음

                # 스위치의 범위를 초과하거나 좌우대칭이 아닌 경우
                if number < i or number + i >= N or switch[number - i] != switch[number + i]:

                    for j in range(number - i + 1, number + i):
                        switch[j] = 1 - switch[j]  # 이전 구간까지의 넓이 반전 (최소 길이 1은 보장됨)

                    break

    for i in range(0, N, 20):  # 20줄씩 끊어서 출력
        print(' '.join(map(str, switch[i:i+20])))


func()
