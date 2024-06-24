import sys
from collections import deque
input = sys.stdin.readline

def solution(n, w, l, weights):
    """
    goal: 모든 트럭이 다리를 건너는 "최단시간" 구하기
    args:
        - n: 트럭의 수
        - w: 다리의 길이
        - l: 다리의 최대 하중
        - weights[i]: i번째 트럭의 무게
    note:
        - 트럭의 순서는 바꿀 수 없으며(>> queue), 트럭의 무게는 서로 같지 않을 수 있음
        - 다리 위에는 w대의 트럭만 동시에 올라갈 수 있음
        - 각 트럭들은 하나의 단위시간에 하나의 단위길이만큼 이동할 수 있음
        - 다리 위에 올라가 있는 트럭들의 무게의 합은 "다리의 최대하중인 l보다 작거나 같아야 함"
        - 다리 위에 "완전히 올라가지 못한 트럭"의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않음
    how:
        - 그리디
        - 대기 중인 트럭, 그리고 다리 위에 있는 트럭들을 관리하는 queue 2개 선언
        - 다리 위 트럭들을 관리하는 queue에는 [트럭의 무게, 현재 위치]를 저장
        - 다리의 상태(길이, 하중)를 확인한 뒤 대기 중인 트럭들을 다리 위로 올림
    """
    # 대기 중인 트럭, 다리 위에 있는 트럭들을 관리하는 큐 생성
    q_wait, q_on_bridge = deque(weights), deque()

    cnt = 0 # 시간
    w_on_bridge = 0 # 다리 위에 있는 트럭들의 무게의 합

    # 대기 중인 트럭이 있거나 다리 위에 트럭이 있다면 아래 구문을 실행
    while q_wait or q_on_bridge:

        if not q_on_bridge: # 다리 위에 아무것도 없다면
            truck = q_wait.popleft() # 대기 중인 트럭을
            q_on_bridge.append([truck, 1]) # 다리 위로 올리고
            w_on_bridge += truck # 무게를 갱신

        else: # 다리 위에 트럭이 있다면
            # 트럭들을 단위길이만큼 이동
            for i in range(len(q_on_bridge)):
                q_on_bridge[i][1] += 1

            # 선두에 있는 트럭이 다리를 벗어났다면
            if q_on_bridge[0][1] > w:
                w_on_bridge -= q_on_bridge[0][0] # 무게를 갱신하고
                q_on_bridge.popleft() # 다리 위에서 뺌

            if q_wait: # 대기 중인 트럭이 있다면
                if w_on_bridge + q_wait[0] <= l: # 전체 하중이 l 이하인지 확인한 뒤
                    truck = q_wait.popleft() # 대기 중인 트럭을
                    q_on_bridge.append([truck, 1]) # 다리 위로 올리고
                    w_on_bridge += truck # 무게를 갱신

            # 대기 중인 트럭이 없다면 다리 위에 있는 트럭들의 상태만 갱신하며 종료

        cnt += 1 # 시간 갱신

    return cnt


if __name__ == "__main__":
    # 입력
    n, w, l = map(int, input().split())
    weights = list(map(int, input().split()))

    # 함수 호출
    res = solution(n, w, l, weights)

    # 결과 출력
    print(res)
