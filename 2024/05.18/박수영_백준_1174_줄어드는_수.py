import sys
input = sys.stdin.readline


def solution(n):
    """
    goal: N번째 작은 줄어드는 수를 출력하기 (없는 경우 -1을 출력)
    note:
        - '음이 아닌 정수'를 '십진법'으로 표기했을 때, '왼쪽에서부터 자리수가 감소'할 때, 그 수를 줄어드는 수로 정의
        - 321, 950은 줄어드는 수이고, 322와 958은 아님
        - 가장 작은 줄어드는 수가 1번째 작은 줄어드는 수 >> 321은 950보다 작은 줄어드는 수
        - N은 1백만보다 작거나 같은 자연수
    how:
        - 백트래킹
        - 모든 경우의 수를 다 찾은 뒤 순서대로 정렬. 이후 검색
    """
    stack = []
    mem = []

    def dfs():
        if stack:
            mem.append(int(''.join(list(map(str, stack)))))

        for i in range(10):
            if not stack or stack[-1] > i:
                stack.append(i)
                dfs()
                stack.pop()

    dfs()
    mem.sort()

    return -1 if len(mem) < n else mem[n-1]


if __name__ == "__main__":
    # 입력
    N = int(input())

    # 함수 호출
    res = solution(N)

    # 결과 출력
    print(res)
