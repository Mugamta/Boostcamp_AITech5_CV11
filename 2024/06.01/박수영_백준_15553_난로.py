import sys
import heapq
input = sys.stdin.readline

def solution(n, k, times):
    """
    goal: 난로가 '켜져 있는 시간'의 '최솟값' 구하기
    note:
        - 친구가 있는 경우에만 난로를 킴
        - N명의 친구는 1 ~ N까지 번호를 가짐
        - i번째 친구는 T_i에 도착하고, T_i + 1에 나감
        - '한 번에 한 명만' 방문할 수 있음
        - 난로는 최대 K번 킬 수 있으며, 가장 처음에 난로는 꺼져있음
    how:
        - 우선순위 큐
        - 전체 난로 가동 시간에서 불필요한 구간 시간을 차감하는 방식으로 구현
            - 차감의 의미 >> 해당 구간에서 난로를 껐다 켠다는 것
            - 처음 한 번은 무조건 켜야 하므로, K-1번 차감
    """
    cnt = (times[-1] + 1) - times[0]
    
    pq = []
    for i in range(n - 1):
        heapq.heappush(pq, -(times[i+1] - (times[i] + 1)))

    for _ in range(k - 1):
        cnt += heapq.heappop(pq)

    return cnt


if __name__ == "__main__":
    # 입력
    N, K = map(int, input().split())
    times = [int(input()) for _ in range(N)]

    # 함수 호출
    res = solution(N, K, times)

    # 결과 출력
    print(res)
