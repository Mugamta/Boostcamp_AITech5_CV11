import sys
input = sys.stdin.readline

def solution(n, switches, m, students):
    """
    goal:
        - 스위치들의 마지막 상태 출력
        - 1번 스위치에서 시작하여 마지막 스위치까지 '한 줄에 20개씩' 출력
        - 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 두기
    note:
        - 학생들은 각각 '1 이상이고 스위치 개수 이하인 자연수'를 보유
        - 자신의 '성별과 받은 수에 따라' 스위치를 조작
        - 남학생: '스위치 번호가 자기가 받은 수의 배수이면' 스위치의 상태를 바꿈
        - 여학생:
            '자기가 받은 수와 같은 번호가 붙은 스위치를 중심'으로, 
            '좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간'을 찾아서, 
            '그 구간에 속한 스위치의 상태를 모두 바꿈'
    how:
        - 구현
    """
    def change_status(e):
        return '1' if e == '0' else '0'

    for gender, number in students:
        # 남학생 >> 본인이 받은 수의 배수에 해당되는 스위치들의 상태를 변경
        if gender == 1:
            for idx in range(number, n + 1, number):
                switches[idx - 1] = change_status(switches[idx - 1])

        # 여학생
        elif gender == 2:
            # 중심 스위치의 상태를 먼저 변경
            center = number - 1
            switches[center] = change_status(switches[center])

            # 좌우 대칭을 확인하면서, 해당되는 스위치들의 상태를 변경
            left, right = center - 1, center + 1
            while left >= 0 and right < n:
                if switches[left] == switches[right]:
                    switches[left] = change_status(switches[left])
                    switches[right] = switches[left]

                else:
                    break

                left -= 1
                right += 1

    return switches


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    switch_status = input().split()
    M = int(input().strip())
    student_status = [tuple(map(int, input().split())) for _ in range(M)]

    # 함수 호출
    res = solution(N, switch_status, M, student_status)

    # 결과 출력
    res = ' '.join(res)
    for i in range(0, N*2, 40):
        print(res[i:i+40])
