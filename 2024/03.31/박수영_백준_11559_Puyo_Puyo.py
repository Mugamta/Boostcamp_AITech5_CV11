# time: 1hr 03m
import sys
from collections import deque
input = sys.stdin.readline

def simul_puyopuyo(_field):
    """
    goal: 상대방의 필드가 주어졌을 때, '연쇄가 몇 번 연속으로 일어날 지' 계산하기
    note:
        - 같은 색 뿌요가 '4개 이상' 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한 꺼번에 없어짐 (1연쇄)
        - 뿌요들이 사라지고 나서 위에 다른 뿌요들이 있다면, '아래대로 떨어짐'
        - 터질 수 있는 뿌요가 여러 그룹이 있다면 '동시에 터져야' 하고, 여러 그룹이 터지더라도 '한 번의 연쇄가 추가'
    how:
        - 구현 + BFS
        - 터뜨릴 수 있는 뿌요가 더 이상 없을 때까지 반복 (while)
    """
    def bfs(_r, _c):
        nonlocal visited

        queue = deque([(_r, _c)])
        crds = []
        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in move:
                nr = cur_r + dr
                nc = cur_c + dc

                # 예외 1: 필드를 벗어남
                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    continue

                # 예외 2: 이미 탐색한 지점
                if visited[nr][nc]:
                    continue

                # 예외 3: 기준색과 다름
                if field[cur_r][cur_c] != field[nr][nc]:
                    continue

                # 예외 4: 빈공간
                if field[nr][nc] == ".":
                    continue

                visited[nr][nc] = True
                queue.append((nr, nc))

                crds.append((nr, nc))

        return crds if len(crds) >= 4 else []
    

    cnt = 0
    h, w = len(_field), len(_field[0])
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        visited = [[False] * w for _ in range(h)]
        mem = []

        # 연쇄 가능 여부 파악
        for r in range(h):
            for c in range(w):
                # 예외 1: 이미 탐색한 지점
                if visited[r][c]:
                    continue
                
                # 예외 2: 빈공간
                if _field[r][c] == ".":
                    continue

                res = bfs(r, c)
                mem.extend(res)

        # 연쇄가 불가능하다면 종료
        if not mem:
            return cnt
        
        # 연쇄가 가능하다면, 폭발
        for rm_r, rm_c in mem:
            _field[rm_r][rm_c] = ""

        # 필드 상태 업데이트 (주의: zip을 사용하면 tuple을 반환함)
        tmp = []
        for column_by in zip(*_field):
            tmp.append(list("".join(column_by).rjust(h, ".")))
        
        for i, row_by in enumerate(zip(*tmp)):
            _field[i] = list(row_by)

        cnt += 1


if __name__ == "__main__":
    # 입력
    field = []
    for _ in range(12):
        field.append(list(input().strip()))

    # 풀이
    ans = simul_puyopuyo(field)
    print(ans)
    