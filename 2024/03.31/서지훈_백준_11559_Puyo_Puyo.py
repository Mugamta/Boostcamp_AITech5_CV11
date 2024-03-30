from collections import deque


def func():
    # 문제의 게임 공간은 72칸이므로 특별한 알고리즘 관찰 불가능
    # 같은 색 뿌요가 상하좌우 -> BFS
    # 한 번의 순회에서 72칸을 순회 + 각 칸에서 상하좌우로 최대 4칸으로 5칸 순회, 360칸
    # 한 번의 순회에서 최소 4칸이 줄어듬 -> 360 + 355 + 350... 0
    # (0 ~ 72) * 5 -> 2628 * 5이므로 모든 순회해도 시간 초과는 발생하지 않음

    # 따라서 매 순간의 뿌요가 터지는 조건을 잘 확인하고, 필드를 잘 덮어씌우는 조건의 문제로 추정

    fields = [list(input()) for _ in range(12)]
    # 주어진 상황에서, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 여러 그룹이라도 동시에 터진다.

    plus_x = [1, -1, 0, 0]
    plus_y = [0, 0, 1, -1]

    # 몇 연쇄인지 카운트
    cnt = 0
    while True:
        # 터진 적이 있는지
        flag = False

        # 기존 필드를 복사하고, 이 필드에서 작업
        tmp_fields = [arr[:] for arr in fields]

        visited = [[False for _ in range(6)] for _ in range(12)]

        # 1. 필드를 순회하며, 같은 색의 뿌요가 4칸 이상 모여있는 곳을 체크한다.
        for y in range(12):
            for x in range(6):
                # 뿌요가 있는 칸이라면
                if tmp_fields[y][x] != '.':

                    # 현재 칸의 색깔
                    color = tmp_fields[y][x]

                    # 방문한 칸 저장
                    locates = []

                    # 현재 칸을 저장
                    dq = deque()
                    dq.append((x, y))
                    visited[y][x] = True
                    locates.append((x, y))

                    tmp_cnt = 1

                    while dq:
                        x, y = dq.popleft()

                        for i in range(4):
                            nx, ny = x + plus_x[i], y + plus_y[i]

                            # 칸을 벗어나지 않으며 방문하지 않은 같은 색인 칸이 있다면
                            if 0 <= nx < 6 and 0 <= ny < 12 and tmp_fields[ny][nx] == color and \
                                    not visited[ny][nx]:

                                dq.append((nx, ny))
                                visited[ny][nx] = True
                                locates.append((nx, ny))
                                tmp_cnt += 1  # 칸의 개수를 늘림

                    # 같은 색의 뿌요가 4개 이상 있다면
                    if tmp_cnt >= 4:
                        flag = True
                        for tmp_x, tmp_y in locates:
                            # 저장된 좌표들의 값을 .으로 덮어씌운다.
                            tmp_fields[tmp_y][tmp_x] = '.'

        # 터진 적이 없다면 더 이상 진행 불가능하므로 종료
        if not flag:
            break

        # 터진 적이 있다면 연쇄 횟수를 증가시킴
        cnt += 1

        # 2. 터진 후, 남은 뿌요들을 아래로 떨어뜨린다.

        # 세로로 아래에 있는 빈 칸들을 순서대로 기록하여, 떠 있는 칸들을 배치한다.
        for x in range(5, -1, -1):
            dq = deque()
            for y in range(11, -1, -1):
                # 빈 칸이면 덱에 추가
                if tmp_fields[y][x] == '.':
                    dq.append((x, y))
                else:
                    # 빈 칸이 아니라면

                    if dq:
                        # 빈 칸인 곳의 좌표가
                        tmp_x, tmp_y = dq.popleft()

                        # 뿌요로 채워지고
                        tmp_fields[tmp_y][tmp_x] = tmp_fields[y][x]

                        # 뿌요가 있던 곳은 빈 칸으로 변한다
                        tmp_fields[y][x] = '.'
                        dq.append((x, y))

        # 뿌요가 터지고 하락한 필드를 다시 복제하여 사용
        fields = [arr[:] for arr in tmp_fields]

    # 연쇄가 일어났으므로 값을 더해줌
    print(cnt)


func()
