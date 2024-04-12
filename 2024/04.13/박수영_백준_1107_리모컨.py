import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def solution(n, m, broken_buttons):
    """
    goal: 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야하는지 구하기
    note:
        - 리모컨에는 0 ~ 9 숫자, +, - 버튼이 존재
        - +를 누르면 현재 채널에서 +1 이동, -를 누르면 현재 채널에서 -1 이동
        - 채널 0에서 -를 누르면 채널은 변하지 않고, 채널은 무한대 만큼 존재
        - 일부 버튼은 고장나있음
        - 시작 채널은 100번
    how:
        - 완전탐색
        - 고장나지 않은 버튼만 사용해서 만들 수 있는, N과 가장 가까운 채널 번호를 먼저 탐색 (핵심)
        - 시간복잡도는 O(10 ** len(N))으로, 최악의 경우 10**6 번 탐색
    """ 
    buttons = [str(i) for i in range(10) if i not in broken_buttons]

    start = 100
    stack = []

    def dfs(lim):
        nonlocal start, stack
        if stack:
            tmp = int(''.join(stack))
            if abs(n - tmp) < abs(n - start):
                start = tmp

            # 목표 채널과 가까운 채널이 여러 개 있다면, 크기가 가장 작은 (== 길이가 가장 짧은) 채널을 선택
            elif abs(n - tmp) == abs(n - start):
                if tmp < start: start = tmp

        # 종료 조건
        if len(stack) == lim:
            return
            
        for b in buttons:
            stack.append(b)
            dfs(lim)
            stack.pop()

    # 999번과 같은 경우, 997번이 아닌 1000번이 더 가까움
    # 이러한 경우에 대처하기 위해서, 목표 채널의 번호 개수 + 1을 탐색 제한으로 설정
    constraint = len(str(n))
    if constraint < 6: constraint += 1

    dfs(lim=constraint)
    
    return min(abs(n - 100), abs(n - start) + len(str(start)))


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    M = int(input().strip())

    broken_buttons = []
    if M: broken_buttons = list(map(int, input().split())) # 고장난 버튼이 없을 수 있음

    # 함수 호출
    res = solution(N, M, broken_buttons)

    # 결과 출력
    print(res)
