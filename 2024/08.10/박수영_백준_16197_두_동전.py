import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, board):
    """
    goal:
        - *두 동전 중 하나만 보드에서 떨어뜨리기* 위해 버튼을 최소 몇 번 눌러야 하는지 구하기
        - 두 동전을 떨어트릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면 -1을 출력
    note:
        - o: 동전 | .: 빈칸 | #: 벽
        - 왼쪽/오른쪽/위/아래 로 움직일 수 있음
        - 버튼을 누르면 두 동전이 **동시에** 이동함
        - 벽이면 이동 X / 이동 방향에 칸이 없으면 바깥으로 떨어짐
        - 그 외의 경우에는 한 칸 이동
        - *이동하려는 칸에 동전이 있는 경우*에도 한 칸 이동
    how:
        - BFS를 활용한 구현
        - 핵심은 두 동전 중 하나만 떨어져야 한다는 것
        - 따라서 두 동전 중 하나라도 움직일 수 있다면, 탐색을 진행
        - 탐색하지 않는 경우는 다음과 같음
            1. 두 동전이 움직이지 않을 때
            2. 두 동전 모두 떨어졌을 때
            3. 버튼 조작 횟수가 10회를 초과했을 때
    """
    # 두 동전의 위치를 구해서, BFS 탐색을 위한 큐 구성하기
    # [[r1, c1, r2, c2, 버튼 조작 횟수, 보드 위 동전 개수]]
    pos_of_coins = []
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'o':
                pos_of_coins.extend([r, c])

    pos_of_coins.extend([0, 2])
    queue = deque([pos_of_coins])

    # BFS 탐색
    def validation(nr, nc, r, c, n_coins):
        # 보드를 벗어난다면 보드 위 동전 개수를 하나 줄이고 반환
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return (nr, nc, n_coins-1)

        # 벽인 경우 입력 인자를 그대로 반환
        if board[nr][nc] == '#':
            return (r, c, n_coins)
        
        # 움직일 수 있다면 새 좌표를 반환        
        return (nr, nc, n_coins)

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r1, c1, r2, c2, \
            push_cnt, coin_on_board = queue.popleft()

        # 버튼 조작 횟수가 10회 이하이면서
        # 보드 위 동전이 한 개라면, 탐색을 조기 종료
        if push_cnt <= 10 and coin_on_board == 1:
            return push_cnt
        
        # (상,하,좌,우로 이동)
        for dr, dc in move:
            # 두 동전의 이동 후 좌표를 구한 뒤
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc

            # 새 좌표에 대한 검증을 진행
            vr1, vc1, vcoin_on_board = validation(nr1, nc1, r1, c1, coin_on_board)
            vr2, vc2, vcoin_on_board = validation(nr2, nc2, r2, c2, vcoin_on_board)

            # 검증 후 정보를 점검했을 때,
            # 1. 버튼 조작 횟수가 10회 미만이면서
            # 2. 보드에 동전이 하나라도 존재하고
            # 3. 두 동전 중 하나라도 움직였다면
            # 탐색을 진행
            if push_cnt < 10 and coin_on_board and \
                ((vr1, vc1) != (r1, c1) or (vr2, vc2) != (r2, c2)):
                queue.append((vr1, vc1, vr2, vc2, push_cnt+1, vcoin_on_board))
        
    return -1

if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    # 함수 호출
    res = solution(N, M, board)

    # 결과 출력
    print(res)
