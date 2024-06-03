import sys
input = sys.stdin.readline

def solution(n_songs, init_v, max_v, v_lst):
    """
    goal: '가능한 마지막 곡의 볼륨 중 최댓값'을 출력(연주가 불가능한 경우 -1을 출력)
    note:
        - v_lst[i]는 offset임. 즉 이전까지의 v를 기준으로 v + v_lst[i] 또는 v - v_lst[i]로 변경이 가능
        - 단 0 이상 max_v 이하라는 조건을 만족해야 함
    how:
        - 다이나믹 프로그래밍(점화식 유형 X)
        - set()을 이용하여 중복되는 값을 제거 >> 탐색 속도 최적화
    """
    # 이전 곡에서 연주할 수 있는 경우의 수들을 기록
    mem = set([init_v])
    
    for v in v_lst:
        tmp = set()

        # mem을 순회하면서 조건에 만족하는 값들만 추가
        for e in mem:
            if 0 <= e + v <= max_v:
                tmp.add(e + v)
            
            if 0 <= e - v <= max_v:
                tmp.add(e - v)

        # tmp가 비어있는 경우 셋리스트 중간에 연주가 불가능하다는 것을 의미
        if not tmp:
            return -1

        # 메모리 초과 방지를 위해 mem을 tmp로 초기화
        mem = tmp

    return max(mem)


if __name__ == "__main__":
    # 입력
    N, S, M = map(int, input().split())
    volumes = list(map(int, input().split()))

    # 함수 호출
    res = solution(N, S, M, volumes)

    # 결과 출력
    print(res)
