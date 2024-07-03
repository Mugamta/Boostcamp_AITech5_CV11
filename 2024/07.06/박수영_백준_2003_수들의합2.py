import sys
input = sys.stdin.readline

def solution(n, m, arr):
    """
    goal: N개의 수로 된 수열 A의 i번째 수부터 j번째 수까지 합이 M이 되는 경우의 수 구하기
    args:
        - 1 <= N <= 10,000
        - 1 <= M <= 300,000,000
        - 1 <= A[x] <= 30,000
    how:
        - 투 포인터
        - 합이 M을 초과하면 앞쪽 포인터를 한 칸 이동, M 미만이면 뒤쪽 포인터를 한 칸 이동
        - 배열을 벗어나거나 앞쪽 포인터가 뒤쪽 포인터를 넘을 때까지 탐색 수행 << 해당 조건 삭제 시 통과 (Ref: https://www.acmicpc.net/board/view/102626)
    """
    pt1, pt2 = 0, 0
    cnt = 0
    now_sum = arr[pt1]

    while pt2 < n:
        if now_sum == m:
            cnt += 1

        if now_sum <= m:
            pt2 += 1
            try: now_sum += arr[pt2]
            except: break
        
        else:
            now_sum -= arr[pt1]
            pt1 += 1

    return cnt


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 함수 호출
    res = solution(N, M, arr)

    # 결과 출력
    print(res)
