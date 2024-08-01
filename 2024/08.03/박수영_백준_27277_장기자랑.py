import sys
from collections import deque
input = sys.stdin.readline

def solution(n, arr):
    """
    goal: 적절한 순서로 n명의 병사들을 배치했을 때, 각 병사가 발휘할 수 있는 실력의 합의 최댓값 구하기
    note:
        - 실력 발휘를 최대로 하기 위해선, a_{i} - a{i-1}이 크게 병사들을 배치하면 됨
        - reference: https://dinae.tistory.com/85
        - 문제 풀이에 필요한 핵심 아이디어는 떠올렸으나, 이것이 모든 경우의 수를 처리할 수 있는지 확신이 서지 않았음.
    """
    # 오름차순으로 정렬
    arr.sort()
    arr = deque(arr)

    # arr에 남은 수 중에서 가장 큰 수, 가장 작은 수 순서대로 pop하여 tmp에 추가(병사를 배치하는 과정)
    tmp = []
    cnt, lim = 1, len(arr)
    while cnt <= lim:
        if (cnt % 2) == 1:
            tmp.append(arr.pop())
        else:
            tmp.append(arr.popleft())

        cnt += 1

    # 실력의 합 계산
    answer = 0
    for i in range(lim):
        if i == 0:
            answer += tmp[i]
            continue

        answer += max(0, tmp[i] - tmp[i-1])

    return answer


if __name__ == "__main__":
    # 입력
    N = int(input())
    arr = list(map(int, input().split()))

    # 함수 호출
    res = solution(N, arr)

    # 결과 출력
    print(res)
