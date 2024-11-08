"""
DP
- 두 문자열의 길이만큼 dp 배열을 초기화
- dp 배열에는 '해당 위치까지 공통 부분 문자열의 길이'를 저장
- 이중 for문을 돌면서 문자를 확인
- 같은 문자를 발견한 경우, 직전 위치의 dp 배열에 1을 더해줌

*참고
- https://dailylifeofdeveloper.tistory.com/114
- https://tyoon9781.tistory.com/entry/python-int-size-28byte
- PyPy3의 integer 크기는 dynamic하게 결정됨(고정되어있지 않음)
"""
def solution(str_a, str_b):
    # 이차원 배열 초기화
    str_a_len, str_b_len = len(str_a), len(str_b)
    dp = [[0] * (str_b_len+1) for _ in range(str_a_len+1)]

    a = 1
    print(a.__sizeof__())

    # 탐색
    for i in range(1, str_a_len+1):
        for j in range(1, str_b_len+1):
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

    return max(map(max, dp))


def main():
    # 입력
    str_a, str_b = input(), input()

    # 함수 호출
    res = solution(str_a, str_b)

    # 결과 출력
    print(res)


if __name__ == "__main__":
    main()
