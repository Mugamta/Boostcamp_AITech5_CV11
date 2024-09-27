
"""
시   간  : 277.65 MS
메 모 리 : 10.4 MB
"""
def get_next_positions(board, loc):  # 현재 위치(loc)에서 다음으로 이동 가능한 위치를 반환한다.
    dRow, dCol = [0, 0, 1, -1], [1, -1, 0, 0]
    next_positions = []
    for d in range(4):
        nr, nc = loc[0] + dRow[d], loc[1] + dCol[d]
        if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
            continue
        elif board[nr][nc] == 0:
            continue
        next_positions.append((nr, nc))
    return next_positions


def search(board, aloc, bloc, turn):  # dfs
    if turn % 2 == 0:
        next_positions = get_next_positions(board, aloc)
    else:
        next_positions = get_next_positions(board, bloc)
        
    if not next_positions:  # 현재 turn의 캐릭터가 이동할 수 없는 경우로 현재 turn의 캐릭터가 패배한다.
        return turn % 2 != 0, turn  # ((A가 이긴다면 True, B가 이긴다면 False), 현재까지 이동한 횟수)

    if aloc == bloc:  # 위에서 현재 캐릭터가 이동할 수 있는지 확인, 따라서 이때 같은 블럭에 상대 캐릭터가 있다면 현재캐릭터 승 
        return turn % 2 == 0, turn + 1

    win, lose = [], []
    if turn % 2 == 0:
        board[aloc[0]][aloc[1]] = 0  # 캐릭터가 이동하면 기존의 자리는 0으로 처리한다.
        for nr, nc in next_positions:
            is_a_win, cnt = search(board, [nr, nc], bloc, turn + 1)
            if is_a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[aloc[0]][aloc[1]] = 1
    else:
        board[bloc[0]][bloc[1]] = 0
        for nr, nc in next_positions:
            is_a_win, cnt = search(board, aloc, [nr, nc], turn + 1)
            if not is_a_win:
                win.append(cnt)
            else:
                lose.append(cnt)
        board[bloc[0]][bloc[1]] = 1

    if win:                             # 승리 O
        return turn % 2 == 0, min(win)  # 빠르게 이기는 방법
    else:                               # 승리 X
        return turn % 2 != 0, max(lose) # 패배중 가장 긴 방법


def solution(board, aloc, bloc):
    winner, answer = search(board, aloc, bloc, 0)
    return answer
