import sys
input = sys.stdin.readline

def solution(n, curves):
    """
    goal: 크기가 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수 구하기
    note:
        - K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것
        - 방향은 0, 1, 2, 3 중 하나
        - 왼쪽 위가 (0, 0), 오른쪽 아래가 (100, 100)
    how:
        - 구현
        1. 좌표 방문 여부를 기록할 100x100 배열 초기화
        2. curves를 기반으로 드래곤 커브 생성
            - 드래곤 커브를 구성하는 선분들의 방향 정보(d)를 stack에 저장
            - stack을 순회하면서 새로운 세대의 드래곤 커브 생성 및 좌표 방문 처리

        3. (0, 0)부터 (99, 99)까지 좌상단 좌표 기준 네 개 좌표를 확인해서 모두 방문했을 때 count
    """
    # 좌표 방문 여부를 기록할 100x100 배열 초기화
    board = [[False] * (100 + 1) for _ in range(100 + 1)]

    # 드래곤 커브 생성
    move = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}

    for x_start, y_start, d, g in curves:
        # 0세대 드래곤 커브의 끝점 계산
        x_end = x_start + move[d][0]
        y_end = y_start + move[d][1]

        # 0세대 드래곤 커브에 대한 방문 처리
        board[y_start][x_start] = True
        board[y_end][x_end] = True

        # 드래곤 커브를 구성하는 선분들의 방향 정보를 저장할 배열 생성
        stack = [d]

        # 세대만큼 반복
        for _ in range(g):
            n_lines = len(stack)
            for i in range(n_lines -1, -1, -1):
                # 새로운 선분의 방향 계산
                nd = (stack[i] + 1) % 4

                # 새로운 선분의 끝점 계산
                x_end += move[nd][0]
                y_end += move[nd][1]

                # 방문 처리 및 배열 업데이트
                board[y_end][x_end] = True
                stack.append(nd)


    # 정사각형 구하기
    cnt = 0
    for y_lu in range(100):
        for x_lu in range(100):
            flag = True
            for dy, dx in [(0, 0), (0, 1), (1, 1), (1, 0)]:
                if not board[y_lu + dy][x_lu + dx]:
                    flag = False
                    break

            if flag:
                cnt += 1

    return cnt


if __name__ == "__main__":
    # 입력
    N = int(input())
    curves = [list(map(int, input().split())) for _ in range(N)]

    # 함수 호출
    res = solution(N, curves)

    # 결과 출력
    print(res)
