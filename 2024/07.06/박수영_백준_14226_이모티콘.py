from collections import deque

def solution(s):
    """
    goal: S개의 이모티콘을 화면에 만드는데 걸리는 시간의 *최솟값을 구하기
    note:
        - 이모티콘 1개가 입력된 상태에서 시작
        - 총 3개의 연산이 존재하며, 모든 연산은 1초가 걸림
            - 화면에 있는 이모티콘 모두를 클립보드로 복사하기(덮어쓰기, 일부 복사 X)
            - 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기(비어있다면 붙여넣기 X)
            - 화면에 있는 이모티콘 중 하나를 삭제하기
    how:
        - Ref: https://ji-gwang.tistory.com/300
    question:
        - BFS의 사용 근거
        - 탐색 범위에 대한 근거
    """
    lim = 10**3
    visited = [[False] * (lim + 1) for _ in range(lim + 1)] # visited[i]: (i개의 이모티콘 제작 여부, i개의 이모티콘 복사 여부)

    queue = deque([(1, 0, 0)]) # (현재 이모티콘 개수, 클립보드에 저장된 이모티콘의 개수, 시간)
    visited[1][0] = True

    while queue:
        screen_old, clip_old, cnt = queue.popleft()
        if screen_old == s:
            return cnt
        
        for i in range(3):
            if i == 0: # 화면에 있는 이모티콘 모두를 클립보드로 복사
                screen, clip = screen_old, screen_old

            elif i == 1: # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
                screen, clip = screen_old + clip_old, clip_old

            else: # 화면에 있는 이모티콘 중 하나를 삭제하기
                screen, clip = screen_old - 1, clip_old

            # 탐색 범위를 벗어나거나, 이미 탐색한 지점이라면 무시
            if screen < 0 or screen >= (lim + 1) or clip < 0 or clip >= (lim + 1) or visited[screen][clip]:
                continue
            
            # 조건을 만족한다면 탐색
            queue.append((screen, clip, cnt + 1))
            visited[screen][clip] = True


if __name__ == "__main__":
    # 입력
    S = int(input())

    # 함수 호출
    res = solution(S)

    # 결과 출력
    print(res)
