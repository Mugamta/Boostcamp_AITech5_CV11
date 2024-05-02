import sys
input = sys.stdin.readline

def solution(n, m, arr):
    """
    goal: 수열 A에서 두 수를 골랐을 때, 그 차이가 M 이상이면서 제일 작은 경우를 구하기
    how:
        - 두 수를 고르고 비교하는 과정에서 O(N**2) 시간복잡도 발생
        - '정렬' 후 투 포인터, 큐/스택 등으로 풀이할 수 있을 듯
    """
    # 오름차순 정렬
    arr.sort()

    # 투 포인터 탐색 구현
    pt1, pt2 = 0, 1
    res = float('inf')
    while pt1 <= pt2 and pt2 < N:
        diff = abs(arr[pt1] - arr[pt2])

        if diff >= M:
            if diff <= res:
                res = diff

            pt1 += 1
        
        else:
            pt2 += 1

        if res == M:
            break
                
    return res


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    A = [int(input().strip()) for _ in range(N)]

    # 함수 호출
    res = solution(N, M, A)

    # 결과 출력
    print(res)
