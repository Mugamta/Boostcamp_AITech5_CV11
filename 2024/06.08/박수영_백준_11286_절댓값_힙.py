import sys
import heapq
input = sys.stdin.readline

def solution(nums):
    """
    goal: 입력에서 0이 주어진 회수만큼 답을 출력
        (단, 배열이 비어있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우 0을 출력) 
    note:
        - x(정수)가 0이 아니라면 배열에 x를 추가
        - x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거
    how:
        - heapq를 활용한 구현
    """
    pq = []

    for num in nums:
        if num:
            heapq.heappush(pq, (abs(num), num))
            continue

        try:
            _, e = heapq.heappop(pq)
            print(e)

        except:
            print(0)            


if __name__ == "__main__":
    # 입력
    N = int(input())
    numbers = [int(input()) for _ in range(N)]

    # 함수 호출 && 결과 출력
    solution(numbers)
