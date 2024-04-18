# time: 13m 47s
import sys
input = sys.stdin.readline

def solution(n, arr):
    """
    goal: 그려진 선(들)의 총 길이를 구하기
    note:
        - 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋는다
        - 이미 선이 있는 위치에 겹쳐서 그리는 것이 가능하다
        - 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다
    how:
        - 그리디?
        - 정렬 이후 순차적으로 계산
        - 기준 원소의 끝점과 다음 원소의 시작점을 비교
            - 작거나 같다면 끝점을 업데이트
            - 크다면 기준 원소의 끝점을 기준으로 선 길이를 계산한 뒤, 다음 원소를 새로운 기준으로 설정
    """
    arr.sort(key=lambda x: (x[0], x[1]))

    total_len = 0
    start, end = 0, 0
    for p1, p2 in arr:
        if not start and not end:
            start, end = p1, p2
            continue

        # 기준 원소의 끝점과 다음 원소의 시작점을 비교
        if p1 <= end:
            if p2 > end:
                end = p2

        else:
            # 기준 원소의 끝점을 기준으로 선 길이를 계산 후 누적
            total_len += (end - start)

            # 기준 원소를 업데이트
            start, end = p1, p2

    # 마지막 선의 길이를 더함
    total_len += (end - start)

    return total_len


if __name__ == "__main__":
    # 입력
    N = int(input().strip())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 함수 호출
    res = solution(N, data)

    # 결과 출력
    print(res)
