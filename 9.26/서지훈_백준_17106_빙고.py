from tqdm.auto import tqdm
import time


def check(bingo, B5=None, log=False):
    row_lines = [True for _ in range(5)]  # 가로줄의 빙고 여부
    row_lines_cnt = 5  # 가로 빙고 개수

    column_lines = [True for _ in range(5)]  # 세로줄의 빙고 여부
    column_lines_cnt = 5  # 세로 빙고 개수

    A5_E1 = True  # 대각선 빙고 여부
    A1_E5 = True

    for y in range(5):
        for x in range(5):
            if bingo[y][x] != '#':
                row_lines[y] = False
                row_lines_cnt -= 1
                break

    for x in range(5):
        for y in range(5):
            if bingo[y][x] != '#':
                column_lines[x] = False
                column_lines_cnt -= 1
                break

    for i in range(5):
        if bingo[i][i] != '#':
            A1_E5 = False
            break

    for i in range(5):
        if bingo[i][4 - i] != '#':
            A5_E1 = False
            break

    # ------------- 빙고 검증 -----------------

    # A1 - A5에서 E1으로 가는 대각선은 빙고 줄이 아니다.
    if bingo[0][0] == '#' and A5_E1:
        if log: print("A1 모순")
        return False
    elif bingo[0][0] != '#' and not A5_E1:
        if log: print("A1 모순")
        return False

    # B1 - 이 칸은 빙고 줄의 일부가 아니다.
    if bingo[0][1] == '#' and (row_lines[0] or column_lines[1]):
        if log: print("B1 모순")
        return False
    elif bingo[0][1] != '#' and not (row_lines[0] or column_lines[1]):
        if log: print("B1 모순")
        return False

    # C1 - A1에서 E5로 가는 대각선은 빙고줄이다.
    if bingo[0][2] == '#' and not A1_E5:
        if log: print("C1 모순")
        return False
    elif bingo[0][2] != '#' and A1_E5:
        if log: print("C1 모순")
        return False

    # D1 - D4는 색칠되어 있다.
    if bingo[0][3] == '#' and bingo[3][3] != '#':
        if log: print("D1 모순")
        return False
    elif bingo[0][3] != '#' and bingo[3][3] == '#':
        if log: print("D1 모순")
        return False

    # E1 - 이 칸은 빙고줄의 일부이다.
    if bingo[0][4] == '#' and not (row_lines[0] or column_lines[4]):
        if log: print("E1 모순")
        return False
    elif bingo[0][4] != '#' and (row_lines[0] or column_lines[4]):
        if log: print("E1 모순")
        return False

    # A2 - A4는 색칠이 안 되어 있다.
    if bingo[1][0] == '#' and bingo[3][0] == '#':
        if log: print("A2 모순")
        return False
    elif bingo[1][0] != '#' and bingo[3][0] != '#':
        if log: print("A2 모순")
        return False

    # B2 - 모든 방향의 빙고 줄이 존재한다.
    if bingo[1][1] == '#' and not (row_lines_cnt >= 1 and column_lines_cnt >= 1 and (A1_E5 or A5_E1)):
        if log: print("B2 모순")
        return False

    elif bingo[1][1] != '#' and (row_lines_cnt >= 1 and column_lines_cnt >= 1 and (A1_E5 or A5_E1)):
        if log: print("B2 모순")
        return False

    # C2 - 이 문장은 참이다. -> 참이여도, 거짓이여도 가능한 문장이므로 검사할 필요는 없다.
    # 굳이 구현한다면 아래와 같다.
    if bingo[1][2] == '#' and bingo[1][2] != '#':
        if log: print("C2 모순")
        return False
    elif bingo[1][2] != '#' and bingo[1][2] == '#':
        if log: print("C2 모순")
        return False

    # D2 - 17개 이하의 칸이 색칠되어 있다.
    black_cnt = 0
    for y in range(5):
        for x in range(5):
            if bingo[y][x] == '#':
                black_cnt += 1

    if bingo[1][3] == '#' and black_cnt > 17:
        if log: print("D2 모순")
        return False
    elif bingo[1][3] != '#' and black_cnt <= 17:
        if log: print("D2 모순")
        return False

    # E2 - 빙고 줄의 일부인 칸은 짝수 개이다.
    bingo_cell = set()
    for i in range(5):
        if row_lines[i]:
            for j in range(5):
                bingo_cell.add(i * 5 + j)
    for i in range(5):
        if column_lines[i]:
            for j in range(5):
                bingo_cell.add(j * 5 + i)
    if A1_E5:
        for i in range(5):
            bingo_cell.add(i * 5 + i)
    if A5_E1:
        for i in range(5):
            bingo_cell.add((i + 1) * 4)

    bingo_cell_cnt = len(bingo_cell)

    if bingo[1][4] == '#' and bingo_cell_cnt % 2 == 1:
        if log: print("E2 모순")
        return False
    elif bingo[1][4] != '#' and bingo_cell_cnt % 2 == 0:
        if log: print("E2 모순")
        return False

    # A3 - 이 칸은 빙고줄의 일부이다.
    if bingo[2][0] == '#' and not (row_lines[2] or column_lines[0]):
        if log: print("A3 모순")
        return False
    elif bingo[2][0] != '#' and (row_lines[2] or column_lines[0]):
        if log: print("A3 모순")
        return False

    # B3 - 색칠되었으나 빙고 줄의 일부가 아닌 칸은 5개 이상이다.
    if bingo[2][1] == '#' and black_cnt - bingo_cell_cnt < 5:
        if log: print("B3 모순")
        return False
    elif bingo[2][1] != '#' and black_cnt - bingo_cell_cnt >= 5:
        if log: print("B3 모순")
        return False

    # C3 - 이 칸은 색칠되지 않았거나 빙고 줄의 일부이다.
    if bingo[2][2] == '#' and not (bingo[2][2] != '#' or (column_lines[2] or row_lines[2] or A1_E5 or A5_E1)):
        if log: print("C3 모순")
        return False
    elif bingo[2][2] != '#' and (bingo[2][2] != '#' or (column_lines[2] or row_lines[2] or A1_E5 or A5_E1)):
        if log: print("C3 모순")
        return False

    # D3 - 세로 빙고 줄은 2개 이상이다.
    if bingo[2][3] == '#' and row_lines_cnt < 2:
        if log: print("D3 모순")
        return False
    elif bingo[2][3] != '#' and row_lines_cnt >= 2:
        if log: print("D3 모순")
        return False

    # E3 - 빙고줄의 일부가 아닌 칸은 10개 이상이다.
    if bingo[2][4] == '#' and 25 - bingo_cell_cnt < 10:
        if log: print("E3 모순")
        return False
    elif bingo[2][4] != '#' and 25 - bingo_cell_cnt >= 10:
        if log: print("E3 모순")
        return False

    # A4 - A2는 색칠이 안 되어 있다.
    if bingo[3][0] == '#' and bingo[1][0] == '#':
        if log: print("A4 모순")
        return False
    elif bingo[3][0] != '#' and bingo[1][0] != '#':
        if log: print("A4 모순")
        return False

    # B4 - 제 2행과 D열 중 적어도 하나는 빙고 줄이다.
    if bingo[3][1] == '#' and not (row_lines[1] or column_lines[3]):
        if log: print("B4 모순")
        return False
    elif bingo[3][1] != '#' and (row_lines[1] or column_lines[3]):
        if log: print("B4 모순")
        return False

    # C4 - C열에는 색칠된 칸이 3개 이하 있다.
    C_column_cnt = 0
    for i in range(5):
        if bingo[i][2] == '#':
            C_column_cnt += 1

    if bingo[3][2] == '#' and C_column_cnt > 3:
        if log: print("C4 모순")
        return False
    elif bingo[3][2] != '#' and C_column_cnt <= 3:
        if log: print("C4 모순")
        return False

    # D4 - D1은 색칠 되어 있다.
    if bingo[3][3] == '#' and bingo[3][0] != '#':
        if log: print("D4 모순")
        return False
    elif bingo[3][3] != '#' and bingo[3][0] == '#':
        if log: print("D4 모순")
        return False

    # E4 - 대각선 빙고 줄이 있다.
    if bingo[3][4] == '#' and not (A1_E5 or A5_E1):
        if log: print("E4 모순")
        return False
    elif bingo[3][4] != '#' and (A1_E5 or A5_E1):
        if log: print("E4 모순")
        return False

    # A5 - E5는 색칠되어 있다.
    if bingo[4][0] == '#' and bingo[4][4] != '#':
        if log: print("A5 모순")
        return False
    elif bingo[4][0] != '#' and bingo[4][4] == '#':
        if log: print("A5 모순")
        return False

    # B5 - 이 문제의 정답은 1개가 아니다 -> 판별 코드 내에서는 알 수 없음.
    if B5 is not None:
        if bingo[4][1] == '#' and not B5:
            if log: print("B5 모순")
            return False
        elif bingo[4][1] != '#' and B5:
            if log: print("B5 모순")
            return False

    # C5 - 이 칸은 색칠되어 있다. -> 참, 거짓에 무관한 칸이므로 구현필요 없음
    if bingo[4][2] == '#' and bingo[4][2] != '#':
        if log: print("C5 모순")
        return False
    elif bingo[4][2] != '#' and bingo[4][2] == '#':
        if log: print("C5 모순")
        return False

    # D5 - 빙고 줄의 개수는 3개 이상이다.
    if bingo[4][3] == '#' and \
            row_lines_cnt + column_lines_cnt + (1 if A1_E5 else 0) + (1 if A5_E1 else 0) < 3:
        if log: print("D5 모순")
        return False
    if bingo[4][3] != '#' and \
            row_lines_cnt + column_lines_cnt + (1 if A1_E5 else 0) + (1 if A5_E1 else 0) >= 3:
        if log: print("D5 모순")
        return False

    # E5 - A5는 색칠되어 있다.
    if bingo[4][4] == '#' and bingo[4][0] != '#':
        if log: print("E5 모순")
        return False
    elif bingo[4][4] != '#' and bingo[4][0] == '#':
        if log: print("E5 모순")
        return False

    return True


def solve():
    # 25칸의 빙고이므로, 2^25의 경우의 수가 가능
    # 0 ~ 24의 칸을 2진수로 표현하여 리스트 만들기

    res = 0
    # for idx in range(2**25):  tqdm을 쓰지 않으려면 이렇게 사용하면 된다.
    for cnt in tqdm(range(2 ** 25)):
        li = [[0 for _ in range(5)] for _ in range(5)]

        for y in range(5):
            for x in range(5):
                li[y][x] = '#' if cnt % 2 == 0 else '.'
                cnt //= 2

        if check(li):
            print()
            for i in li:
                print(i)
            print("위 빙고는 성립 가능성이 있다.\n")
            res += 1

    # 이 문제의 정답이 1개라면 B5는 거짓
    # 이 문제의 정답이 1개가 아니라면 B5는 참

    print("---------------------------------------------------------")

    if res == 1:
        print("조건에 맞는 빙고가 한 개 이므로, B5가 검은 칸이 아니라면 위 빙고가 정답이다.")
    elif res > 1:
        print("조건에 맞는 빙고가 여러개이므로, B5의 조건에 따라 분기하자.")
        print("우선, B5가 참인 경우를 보자.")
        time.sleep(0.1)

        # B5가 참인 경우 - 문제의 정답이 1개가 아니여야 함
        res = 0
        for cnt in tqdm(range(2 ** 25)):
            li = [[0 for _ in range(5)] for _ in range(5)]

            for y in range(5):
                for x in range(5):
                    li[y][x] = '#' if cnt % 2 == 0 else '.'
                    cnt //= 2

            if li[4][1] != '#':  # B5가 참인 경우만 검사
                continue

            if check(li):
                print()
                for i in li:
                    print(i)
                print("B5가 참인 경우, 위 빙고는 성립 가능성이 있다.\n")
                res += 1
        if res <= 1:
            print("B5가 참이지만 정답의 개수가 1개 이하이므로, 위 빙고는 모순된다.")
        else:
            print("B5는 참이므로, 위 빙고는 정답 중 일부이다.")

        # B5가 거짓인 경우 - 문제의 정답이 1개여야 함
        print("-------------------------------------------------")
        print("\n다음으로, B5가 거짓인 경우를 보자.")
        time.sleep(0.1)
        res = 0
        for cnt in tqdm(range(2 ** 25)):
            li = [[0 for _ in range(5)] for _ in range(5)]

            for y in range(5):
                for x in range(5):
                    li[y][x] = '#' if cnt % 2 == 0 else '.'
                    cnt //= 2

            if li[4][1] != '.':  # B5가 거짓인 경우만 검사
                continue

            if check(li):
                print()
                for i in li:
                    print(i)
                print("B5가 거짓인 경우, 위 빙고는 성립 가능성이 있다.\n")
                res += 1
        if res >= 2:
            print("B5가 거짓이지만 정답의 개수가 2개 이상이므로, 위 빙고들은 모순된다.")
        else:
            print("B5는 거짓이므로, 위 빙고는 유일한 정답이다.")

    else:
        print("조건 설정에 문제가 있어 정답인 빙고를 찾지 못함")


solve()
