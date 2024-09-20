import sys
input = sys.stdin.readline

def solution(n, pref_dict):
    """
    goal: 만족도의 총 합 구하기
    note:
        - 중심 칸을 기준으로 상하좌우에 있는 칸만 인접한 것으로 정의
        - 학생의 자리를 정하는 기준
            1. *비어있는 칸* 중에서 *좋아하는 학생이 인접한 칸에 가장 많은 칸*으로 자리를 정함
            2. 1을 만족하는 칸이 여러 개면, 인접한 칸 중 *비어있는 칸이 가장 많은 칸*으로 자리를 정함
            3. 2를 만족하는 칸도 여러 개면, (행 번호, 열 번호)가 작은 순서대로 자리를 정함
        - 자리 배치가 모두 끝나면, *만족도*를 계산
            - 만족도는 특정 학생과 인접한 칸에 앉은 *좋아하는 학생의 수*를 기반으로 계산
            - 0명이면 0, 1명이면 1, 2명이면 10, 3명이면 100, 4명이면 1000
    how:
        - 단순 구현 (만족도의 최댓값을 구하는 게 아니기 때문)
        - 자리 정하기
            - 순서대로 교실 전체를 탐색하되, 빈 칸을 찾아서 
                (좋아하는 학생이 인접한 칸에 있는 경우의 수, 비어있는 칸의 수)를 계산
            - 조건에 만족하는 칸에 해당 학생의 번호를 기록함

        - 만족도 구하기
            - 상하좌우 탐색해서 좋아하는 학생이 인접해있는 칸의 수를 세고, 만족도를 계산하면 됨
    """
    classroom = [[0] * n for _ in range(n)]
    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ### 자리 정하기 ###
    for student, p_list in pref_dict.items():
        # 위치 및 주변 정보
        best_r, best_c = 0, 0

        # note: 빈 칸이지만 조건을 하나도 만족하지 않는 경우가 있을 수 있음 >> -1로 초기화
        best_n_like, best_n_empty = -1, -1

        # 모든 위치 탐색
        for r in range(n):
            for c in range(n):
                # 빈 자리가 아니면 무시
                if classroom[r][c]:
                    continue

                # 인접 칸 확인
                n_like, n_empty = 0, 0

                for dr, dc in adj:
                    nr = r + dr
                    nc = c + dc

                    # 범위 밖 >> 예외처리
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue
                    
                    if not classroom[nr][nc]: # 빈 칸
                        n_empty += 1
                    
                    else:
                        # 인접한 칸에 좋아하는 학생이 있음
                        if classroom[nr][nc] in p_list:
                            n_like += 1

                # 비교 후 값 갱신
                if (n_like > best_n_like) or \
                    (n_like == best_n_like and n_empty > best_n_empty):
                    best_r, best_c = r, c
                    best_n_like, best_n_empty = n_like, n_empty

        # 교실 정보 갱신
        classroom[best_r][best_c] = student

    ### 만족도 계산하기 ###
    score = 0

    for r in range(n):
        for c in range(n):
            student = classroom[r][c]
            n_like = 0

            # 인접한 칸 탐색
            for dr, dc in adj:
                nr = r + dr
                nc = c + dc

                # 범위 밖 >> 예외처리
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue

                # 좋아하는 학생의 수 세기
                if classroom[nr][nc] in pref_dict[student]:
                    n_like += 1

            if n_like: score += (10**(n_like - 1))

    return score


if __name__ == "__main__":
    # 입력
    N = int(input())
    preference = {}
    for _ in range(N**2):
        student, p1, p2, p3, p4 = map(int, input().split())
        preference[student] = [p1, p2, p3, p4]

    # 함수 호출
    res = solution(N, preference)

    # 결과 출력
    print(res)
