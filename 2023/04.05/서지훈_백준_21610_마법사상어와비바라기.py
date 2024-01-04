"""
13:16 문제 읽기 시작
8방향 이동을 보면 탐색 문제같으나
세부적인 조건 묘사를 보면 구현 - 시뮬레이션 형 문제
단순히 구현을 하면 됨

13:17 코드 구현 시작
"""


def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    clouds = {(0, N-1), (1, N-1), (0, N-2), (1, N-2)}  # (x, y)

    for _ in range(M):
        d, s = map(int, input().split())
        d -= 1

        plus_x = [-1, -1, 0, 1, 1, 1, 0, -1]
        plus_y = [0, -1, -1, -1, 0, 1, 1, 1]

        new_clouds = set()

        # 1. 모든 구름이 d 방향으로 s칸 이동
        for cloud in clouds:
            new_clouds.add(((cloud[0] + s * plus_x[d] + 50 * N) % N, (cloud[1] + s * plus_y[d] + 50 * N) % N))
            # 좌표 초과를 방지로 N을 더하여 나머지 연산 - 0 = 0, -1 = N-1, -2 = N-2

        # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        for cloud in new_clouds:
            A[cloud[1]][cloud[0]] += 1

        # 3, 4. 구름이 모두 사라지고, 2에서 물이 증가한 칸에 물 복사버그를 시전한다.
        # 즉, 구름이 있던 칸에서, 경계를 넘어가지 않는 1칸 대각선 칸에 있는 최대 네 개의 바구니 중, 물이 차 있는 바구니의 수
        for cloud in new_clouds:  # 구름의 좌표와 같으므로 이를 사용
            plus_x = [-1, 1, 1, -1]
            plus_y = [1, 1, -1, -1]

            for i in range(4):
                x = cloud[0] + plus_x[i]
                y = cloud[1] + plus_y[i]

                if 0 <= x < N and 0 <= y < N and A[y][x] > 0:
                    A[cloud[1]][cloud[0]] += 1

        # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
        # 이때 칸 3에서 구름이 사라진 칸은 제외함

        clouds.clear()
        for y in range(N):
            for x in range(N):
                if (x, y) not in new_clouds and A[y][x] >= 2:  # 칸 3에서 구름이 사라진 칸이 아니며 물의 양이 2 이상
                    clouds.add((x, y))  # 구름이 생기고
                    A[y][x] -= 2  # 물의 양이 2 줄어든다

    # M 번의 이동이 모두 끝난 후
    result = 0
    for y in range(N):
        for x in range(N):
            result += A[y][x]  # 바구니에 들어있는 물의 총 합
    print(result)


main()