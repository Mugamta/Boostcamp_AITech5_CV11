# time: 24m 03s
import sys
import heapq
input = sys.stdin.readline

def solution(n, arr):
    """
    goal: 강의실 개소를 '최소'로 해서 모든 수업이 가능하도록 만들기
    note:
        - s_i에 시작해서 t_i에 끝남
        - 수업이 끝난 직후에 다음 수업을 시작할 수 있ㅇ므
    how:
        - 강의실 개수를 최소로 쓰려면, 같은 강의실에 최대한 수업을 많이 넣으면 됨
        - 같은 강의실에 넣으려면 이전 수업과 겹치는지 확인해야 하는데, 여기서 불필요한 연산이 많이 발생함
        - heapq를 사용할 것
        - 먼저 배열을 정렬 (시작 시간이 빠른 순, 종료 시간이 빠른 순)
        - 진행 중인 수업을 저장할 heapq 배열을 선언. 종료 시간이 기준인 min heap
        - 새로 시작할 수업의 시작 시간과 min heap의 첫 번째 값을 비교했을 때, 이상이면 pop 미만이면 push
        - heapq의 길이가 강의실의 개수
    """
    # 배열 정렬
    arr.sort(key=lambda x: (x[0], x[1]))

    # 메인 알고리즘
    pq = []
    for s, t in arr:
        if not pq:
            heapq.heappush(pq, t)
            continue

        if s >= pq[0]:
            heapq.heappop(pq)

        heapq.heappush(pq, t)

    return len(pq)


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, arr))
