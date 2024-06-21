import sys
from collections import deque
input = sys.stdin.readline

def solution(n, a, b):
    """
    goal: 
        - **사전 순으로 가장 앞서는** N개의 건물 높이 정보를 출력하기
        - 공백으로 구분해서 출력해야 하며, 출력하는 수들이 모두 같아도 됨
        - 높이는 1보다 크거나 같은 정수여야 함
        - 존재하지 않는 경우 -1을 출력
    note:
        - 다양한 높이의 건물들이 n개 존재
        - 건물 왼쪽: 가희, 건물 오른쪽: 단비
        - 가희와 단비, 건물들은 아래와 같은 순서로 배치되어 있음
            - 가희의 오른쪽에는 1번 건물이 있음
            - x가 1이상 N-1이하의 정수일 때, x번 건물의 오른쪽에는 x+1번 건물이 있음
            - N번 건물의 오른쪽에는 단비가 있음
        - 가희와 단비가 볼 수 있는 건물은 아래와 같음
            - 가희는 1번 건물을 볼 수 있음
            - k번 건물보다 왼쪽에 있는 건물들이 모두 k번 건물보다 높이가 낮다면, 가희는 k번 건물을 볼 수 있음
            - 단비는 N번 건물을 볼 수 있음
            - k번 건물보다 오른쪽에 있는 건물들이 모두 k번 건물보다 높이가 낮다면, 단비는 k번 건물을 볼 수 있음
    args:
        - n: 건물의 개수 (1이상 10*5이하)
        - a: **가희가 볼 수 있는** 건물의 개수 (1이상 n이하)
        - b: **단비가 볼 수 있는** 건물의 개수 (1이상 n이하)
    how:
        - 그리디 알고리즘
        - Reference: https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-24337-%EA%B0%80%ED%9D%AC%EC%99%80-%ED%83%91-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    """
    buildings = deque()
    height = 1

    for _ in range(a - 1):
        buildings.append(height)
        height += 1

    buildings.append(max(a, b))

    height = b - 1
    for _ in range(b - 1):
        buildings.append(height)
        height -= 1

    if len(buildings) > n:
        return [-1]
    
    tmp = buildings.popleft()
    for _ in range(n - len(buildings) - 1):
        buildings.appendleft(1)

    buildings.appendleft(tmp)

    return buildings


if __name__ == "__main__":
    # 입력
    n, a, b = map(int, input().split())

    # 함수 호출
    res = solution(n, a, b)

    # 결과 출력
    print(*res)
    