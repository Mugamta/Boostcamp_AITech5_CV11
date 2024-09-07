import sys
input = sys.stdin.readline

class MonitoringSystem:
    """
    goal: T초가 지난 후 방에 남아있는 미세먼지의 양 구하기
    how:
        - 구현
    """
    def __init__(self, R, C, T, room_status):
        self.r = R
        self.c = C
        self.t = T

        self.room_status = room_status

        # 미세먼지 확산 및 공기 이동 방향(우, 상, 좌, 하)
        self.move = [(0, 1), (-1, 0), (0, -1), (1, 0)] 

        # 공기청정기 위치 구해두기
        self.air_cleaner = []
        for r in range(R):
            if self.room_status[r][0] == -1:
                self.air_cleaner.append((r, 0))
                self.air_cleaner.append((r+1, 0))
                break

    def diffusion(self, ):
        """
        note:
            - 인접한 네 방향으로 확산하는데, 미세먼지가 있는 모든 칸에서 **동시에** 일어남
            - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 X
            - 확산되는 양은 1/5이고, 소수점은 버림
            - 남은 양은 원래 양 - 확산되는 양 * 확산된 방향의 개수
        """
        # 동시에 확산한다는 조건을 만족하기 위해 새로운 배열 생성
        self.tmp = [[0] * self.c for _ in range(self.r)]

        for r in range(self.r):
            for c in range(self.c):
                # 예외 1: 빈 칸인 경우
                if self.room_status[r][c] == 0:
                    continue

                # 예외 2: 공기청정기인 경우
                if self.room_status[r][c] == -1:
                    self.tmp[r][c] = -1
                    continue

                # 확산
                n_diffusions = 0 # 확산 횟수
                for dr, dc in self.move:
                    nr = r + dr
                    nc = c + dc

                    # 예외 1: 칸이 없는 경우
                    if nr < 0 or nr >= self.r or nc < 0 or nc >= self.c:
                        continue

                    # 예외 2: 공기청정기인 경우
                    if self.room_status[nr][nc] == -1:
                        continue
                    
                    # A_{r,c}를 기준으로 확산 진행
                    self.tmp[nr][nc] += int(self.room_status[r][c] / 5)
                    n_diffusions += 1

                # A_{r,c} 업데이트
                self.tmp[r][c] += self.room_status[r][c] - \
                    (int(self.room_status[r][c] / 5) * n_diffusions)
                
        # 방 상태 업데이트
        self.room_status = self.tmp

    def cleaning(self, mode='ccw'):
        """
        note:
            - 공기청정기 기준 위쪽은 반시계방향으로 바람이 순환(아래쪽은 시계방향으로 순환)
            - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
            - 공기청정기에서 부는 바람은 미세먼지가 없으며, 공기청정기로 들어간 미세먼지는 사라짐
        how:
            - 한 칸씩 밀어주는 걸 구현하면 됨
        """
        # 시작점 구하기
        if mode == 'ccw': r, c = self.air_cleaner[0]
        elif mode == 'cw': r, c = self.air_cleaner[1]

        d = 0 # 방향
        prev = 0 # 초기값

        while True:
            # 새 위치를 구함
            dr, dc = self.move[d]
            nr, nc = r + dr, c + dc

            # 초기 위치(공기청정기)로 돌아오면 종료
            if (nr, nc) in self.air_cleaner:
                break
            
            # 범위 벗어나면 방향을 전환
            if nr < 0 or nr >= self.r or nc < 0 or nc >= self.c:
                if mode == 'ccw': # 반시계 (우 > 상 > 좌 > 하)
                    d = (d + 1) % 4 
                
                elif mode == 'cw': # 시계 (우 > 하 > 좌> 상)
                    d = (d - 1) % 4

                continue
            
            # 이전 위치의 값을 현재 위치에 기록
            backup = self.room_status[nr][nc]
            self.room_status[nr][nc] = prev

            # 현재 위치의 값을 기록
            prev = backup

            # 위치 업데이트
            r, c = nr, nc
        
    def working(self, ):
        t = 0

        # self.t초 동안 공기청정기 작동
        while t < self.t:
            self.diffusion() # 확산

            self.cleaning(mode='ccw') # 반시계 순환
            self.cleaning(mode='cw') # 시계 순환

            t += 1

        # 남아있는 미세먼지의 합 구하기
        result = 0
        for arr in self.room_status:
            for e in arr:
                if e and e != -1:
                    result += e

        return result


if __name__ == "__main__":
    # 입력
    R, C, T = map(int, input().split())
    room_status = [list(map(int, input().split())) for _ in range(R)]

    # 함수 호출
    ms = MonitoringSystem(R, C, T, room_status)
    res = ms.working()

    # 결과 출력
    print(res)
